import pyautogui
import os
import tkinter as tk
from datetime import datetime
from multiprocessing import Process

def popup_worker(text):
    try:
        root = tk.Tk()
        root.withdraw() # Completely hides the background master window framework
        
        top = tk.Toplevel(root)
        top.attributes("-topmost", True) # Forces the pill to float above all apps
        top.config(bg="#111111")
        
        # Determine dynamic screen location coordinates
        screen_width = top.winfo_screenwidth()
        x_coord = screen_width - 360  # 360px out from the right screen edge
        y_coord = 50                  # 50px down from the top edge
        top.geometry(f"320x60+{x_coord}+{y_coord}")
        
        # --- THE FIX: Force render order initialization to strip all borders ---
        top.update_idletasks()
        top.overrideredirect(True) # Cuts out the white "tk" title bar and close button completely
        
        # Build canvas rendering pipeline
        canvas = tk.Canvas(top, width=320, height=60, bg="#111111", highlightthickness=0)
        canvas.pack()
        
        # Generate the smooth rounded blue notification pill vector layout geometry
        points = [20, 5, 300, 5, 315, 20, 315, 40, 300, 55, 20, 55, 5, 40, 5, 20]
        canvas.create_polygon(points, fill="#0078D7", smooth=True)
        canvas.create_text(160, 30, text=text, fill="white", font=("Segoe UI", 12, "bold"))
        
        # Match system alpha blend windows composite parameters for transparency integration
        top.wm_attributes("-transparentcolor", "#111111")
        
        top.lift()
        top.update()
        
        # Terminate and close after precisely 2 seconds
        root.after(2000, root.destroy)
        root.mainloop()
    except Exception as e:
        print(f"Popup failure: {e}")

def take_screenshot():
    folder = "Screenshots"
    if not os.path.exists(folder): 
        os.makedirs(folder)
        
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
    filepath = os.path.join(folder, filename)
    
    pyautogui.screenshot(filepath)
    print(f"📸 Screenshot compiled to: {filepath}")
    
    # Detach as background multiprocessing execution sequence thread
    p = Process(target=popup_worker, args=("📸 SCREENSHOT SAVED",))
    p.daemon = True
    p.start()