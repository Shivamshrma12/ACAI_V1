# 🚀 ACAI_V1 — AI-Powered Hand Gesture Control System

![Python](https://img.shields.io/badge/Python-3.14+-blue)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.35-green)
![OpenCV](https://img.shields.io/badge/OpenCV-Latest-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Transform your webcam into a touchless computer controller using real-time Computer Vision and AI-powered hand gesture recognition.

ACAI_V1 (Advanced Computer-Aided Interaction) is a real-time gesture control system built with Google's MediaPipe Hand Landmarker and OpenCV. The application detects hand gestures through a webcam feed and converts them into system-level actions such as screenshots, media controls, application navigation, and desktop management.

---

# 🎯 Features

### 🔵 Right Hand — Productivity Controls

| Gesture                         | Action                             |
| :------------------------------ | :--------------------------------- |
| **✌️ Peace Sign**               | Capture Screenshot                 |
| **☝️ Index Swipe Left / Right** | Switch Browser or Application Tabs |
| **🖐️ Four-Finger Down Sweep**  | Show Desktop (`Win + D`)           |

### 🔴 Left Hand — Media Controls

| Gesture           | Action                     |
| :---------------- | :------------------------- |
| **✌️ Peace Sign** | Mute / Unmute System Audio |
| **🖐️ Open Palm** | Play / Pause Media         |

---


# 🛠 Technology Stack

* Python 3.14+
* OpenCV
* MediaPipe Tasks API
* PyAutoGUI
* Tkinter
* Multiprocessing

---

# 🧠 Skills Demonstrated

* Computer Vision
* Real-Time Hand Tracking
* Gesture Recognition
* Human Computer Interaction (HCI)
* AI-Based Input Systems
* OpenCV Development
* Multi-Processing
* System Automation
* Event-Driven Programming
* Python Application Development

---

# ⚙️ System Architecture

## main.py

Handles:

* Webcam stream acquisition
* Gesture processing loop
* Action cooldown management
* System command execution

## hand_tracker.py

Handles:

* MediaPipe HandLandmarker integration
* Landmark detection
* Hand skeleton rendering
* Gesture data extraction

## utils.py

Handles:

* Notification rendering
* Screenshot alerts
* Background process management
* Non-blocking UI operations

---

# 🔥 Engineering Highlights

### Real-Time Performance

Optimized gesture recognition pipeline with minimal latency for smooth and responsive user interaction.

### False Trigger Prevention

Implements gesture validation logic and hold-time detection to reduce accidental activations.

### Multi-Process Notification System

Uses Python multiprocessing to prevent GUI notifications from interrupting the vision pipeline.

### Dynamic Screen Adaptation

Automatically adjusts notification placement according to display resolution.

### Automated Screenshot Workflow

Captured screenshots are instantly saved and accompanied by a floating notification overlay.

---

# 📂 Project Structure

```text
ACAI_V1/
│
├── main.py
├── hand_tracker.py
├── utils.py
├── hand_landmarker.task
├── screenshots/
└── README.md
```

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Shivamshrma12/ACAI_V1.git
cd ACAI_V1
```

## 2. Install Dependencies

```bash
pip install opencv-python mediapipe==0.10.35 pyautogui
```

## 3. Run the Application

```bash
python main.py
```

---

# 📋 Requirements

* Python 3.14+
* Webcam
* Windows Operating System
* Internet connection (first launch only)

> On first execution, MediaPipe automatically downloads the required hand tracking model (`hand_landmarker.task`). Future launches start immediately.

---

# 📈 Project Status

| Feature                     | Status     |
| :-------------------------- | :--------- |
| Hand Tracking Engine        | ✅ Complete |
| Screenshot Automation       | ✅ Complete |
| Media Controls              | ✅ Complete |
| Tab Navigation              | ✅ Complete |
| Desktop Management          | ✅ Complete |
| Custom Gesture Training     | 🔄 Planned |
| Voice + Gesture Integration | 🔄 Planned |
| Gesture Personalization     | 🔄 Planned |

---

# 💡 Potential Applications

* Touchless Computer Interaction
* Productivity Automation
* Accessibility Solutions
* Smart Workstations
* Human-Computer Interaction Research
* AI-Powered Desktop Control

---

# 🤝 Contributing

Contributions, feature requests, and suggestions are welcome.

Feel free to fork the repository and submit pull requests for improvements.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Shivam Sharma**

B.Tech Student | AI & Computer Vision Enthusiast

Passionate about building practical AI systems that bridge human interaction and intelligent automation.
