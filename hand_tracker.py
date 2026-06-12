import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import os
import urllib.request

class HandDetector:
    def __init__(self, mode=False, max_hands=2, detection_con=0.5, track_con=0.5):
        model_path = "hand_landmarker.task"
        if not os.path.exists(model_path):
            print("Downloading tracking asset model file from Google... please wait...")
            url = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
            urllib.request.urlretrieve(url, model_path)

        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=max_hands,
            min_hand_detection_confidence=detection_con,
            min_hand_presence_confidence=track_con
        )
        self.detector = vision.HandLandmarker.create_from_options(options)
        self.results = None
        
        # Hardcoded connections to draw the skeleton lines manually
        self.connections = [
            (0, 1), (1, 2), (2, 3), (3, 4),      # Thumb
            (0, 5), (5, 6), (6, 7), (7, 8),      # Index
            (5, 9), (9, 10), (10, 11), (11, 12),  # Middle
            (9, 13), (13, 14), (14, 15), (15, 16),# Ring
            (13, 17), (0, 17), (17, 18), (18, 19), (19, 20) # Pinky
        ]

    def find_hands(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)
        self.results = self.detector.detect(mp_image)
        
        if draw and self.results.hand_landmarks:
            for hand_landmarks in self.results.hand_landmarks:
                h, w, _ = img.shape
                points = [(int(lm.x * w), int(lm.y * h)) for lm in hand_landmarks]
                
                # Draw skeleton lines
                for connection in self.connections:
                    p1, p2 = points[connection[0]], points[connection[1]]
                    cv2.line(img, p1, p2, (0, 255, 0), 2)
                    
                # Draw joint dots
                for pt in points:
                    cv2.circle(img, pt, 4, (0, 0, 255), cv2.FILLED)
        return img

    def get_hand_info(self, img):
        hands_data = []
        if self.results and self.results.hand_landmarks:
            for i, hand_landmarks in enumerate(self.results.hand_landmarks):
                label = self.results.handedness[i][0].category_name
                label = "Right" if label == "Left" else "Left" # Compensate for flipping
                
                lm_list = []
                for lm in hand_landmarks:
                    h, w, _ = img.shape
                    lm_list.append([int(lm.x * w), int(lm.y * h)])
                
                hands_data.append({"label": label, "lm_list": lm_list})
        return hands_data