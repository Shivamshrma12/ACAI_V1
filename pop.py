# popup.py
import tkinter as tk

def create_window():
    root = tk.Tk()
    root.overrideredirect(True)  # Remove window borders
    root.attributes("-topmost", True)  # Force over games/Word/YouTube
    root.attributes("-alpha", 0.9)  # Sleek transparency
    
    # Calculate bottom-right position
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = screen_width - 320  
    y = screen_height - 120 
    
    root.geometry(f"300x60+{x}+{y}")
    root.configure(bg="#0f0f0f") 
    
    label = tk.Label(root, text="📸 SCREENSHOT SAVED", 
                     fg="#00ffff", bg="#0f0f0f", 
                     font=("Consolas", 14, "bold"))
    label.pack(expand=True, fill="both")
    
    # Destroy automatically after 2 seconds
    root.after(2000, root.destroy)
    root.mainloop()

if __name__ == "__main__":
    create_window()