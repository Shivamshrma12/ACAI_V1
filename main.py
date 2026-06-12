import cv2
import time
import numpy as np
import pyautogui
import multiprocessing
from hand_tracker import HandDetector 
from utils import take_screenshot

def main():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    detector = HandDetector(max_hands=2, detection_con=0.5, track_con=0.5)

    cooldowns = {"nav": 0, "media": 0, "ss": 0}
    x_history, y_history = [], []
    
    # Tracking states for the right hand peace sign
    peace_start_time = 0
    is_holding_peace = False

    print("🚀 ACAI V13.4: STABILIZED GESTURE FILTERS")

    while True:
        success, frame = cap.read()
        if not success: break
        
        img = cv2.flip(frame, 1) 
        img = detector.find_hands(img, draw=True)
        hands_info = detector.get_hand_info(img)
        curr = time.time()

        for hand in hands_info:
            label = hand["label"]
            lm = hand["lm_list"]
            
            # Tracking finger extensions: Index[8], Middle[12], Ring[16], Pinky[20]
            f_up = [1 if lm[id][1] < lm[id-2][1] else 0 for id in [8, 12, 16, 20]]
            total_f = f_up.count(1)
            
            # Strictly track if Thumb [4] is folded (closer to the hand center horizontally)
            thumb_folded = abs(lm[4][0] - lm[5][0]) < 40

            # ==========================================
            # 🔵 RIGHT HAND ROLE (NAV, SCREENSHOT, MINIMIZE)
            # ==========================================
            if label == "Right":
                # 1. FIXED: STABLE SCREENSHOT (Strict Peace Sign + 0.3s Intent Hold)
                # Requires Index and Middle UP, while Ring, Pinky, and Thumb are strictly DOWN
                if f_up[0] == 1 and f_up[1] == 1 and f_up[2] == 0 and f_up[3] == 0 and thumb_folded:
                    if not is_holding_peace:
                        is_holding_peace = True
                        peace_start_time = curr
                    elif (curr - peace_start_time) >= 0.3: # Must hold intentionally for 0.3 seconds
                        if curr > cooldowns["ss"]:
                            print("📸 STABLE SCREENSHOT CAPTURED!")
                            take_screenshot()
                            cooldowns["ss"] = curr + 4.0  # Safe 4-second cooldown period
                            is_holding_peace = False
                            y_history, x_history = [], []
                else:
                    is_holding_peace = False # Reset if your fingers break form

                # 2. MINIMIZE / SHOW DESKTOP (Sweep Down with 4 Fingers)
                if total_f == 4 and not is_holding_peace:
                    y_history.append(lm[9][1])
                    if len(y_history) > 5: y_history.pop(0)
                    
                    if len(y_history) >= 2 and curr > cooldowns["media"]:
                        move_y = y_history[-1] - y_history[0]
                        if move_y > 80:
                            pyautogui.hotkey('win', 'd')
                            cooldowns["media"] = curr + 1.5
                            y_history = []
                
                # 3. NAVIGATION (Index Finger Swipe Left/Right)
                elif f_up[0] == 1 and f_up[1] == 0 and not is_holding_peace:
                    x_history.append(lm[8][0])
                    if len(x_history) > 5: x_history.pop(0)
                    
                    if len(x_history) >= 2 and curr > cooldowns["nav"]:
                        move_x = x_history[-1] - x_history[0]
                        if abs(move_x) > 50: 
                            if move_x > 0: pyautogui.hotkey('ctrl', 'tab')
                            else: pyautogui.hotkey('ctrl', 'shift', 'tab')
                            cooldowns["nav"] = curr + 0.7
                            x_history = []
                else: 
                    x_history = []
                    y_history = []

            # ==========================================
            # 🔴 LEFT HAND ROLE (MEDIA PLAY/PAUSE & MUTE)
            # ==========================================
            if label == "Left":
                if total_f == 2 and f_up[0] == 1 and f_up[1] == 1 and f_up[2] == 0 and f_up[3] == 0:
                    if curr > cooldowns["media"]:
                        pyautogui.press('volumemute')
                        cooldowns["media"] = curr + 1.2
                
                elif total_f >= 3 and curr > cooldowns["media"]:
                    pyautogui.press('playpause')
                    cooldowns["media"] = curr + 1.2

        cv2.imshow("ACAI V13.4", img)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()