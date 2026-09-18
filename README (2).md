# 🎨 AI Virtual Painter

> A touchless drawing application that uses hand gestures to create digital artwork through a webcam.

## 📌 Project Overview

AI Virtual Painter is a computer vision project developed using Python. It allows users to draw on a virtual canvas without using a mouse, keyboard, or touchscreen.

The application uses a webcam to capture live video and MediaPipe to detect hand movements. The index finger works as a virtual brush, while raising two fingers activates the eraser.

OpenCV processes the camera frames and displays the drawing on the live video. This project shows how artificial intelligence and computer vision can be used to create a simple and interactive application.

## ✨ Features

- 🖐️ Real-time hand tracking
- ✍️ Drawing using the index finger
- 🧽 Erasing using two fingers
- 🎥 Live webcam-based interaction
- 🖼️ Virtual canvas drawing
- 🔄 Smooth line drawing
- 🧠 Hand landmark detection using MediaPipe
- 🧹 Clear the canvas using the `C` key
- ❌ Exit the application using the `Q` key

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenCV | Webcam access and image processing |
| MediaPipe | Hand tracking and finger detection |
| NumPy | Creating and managing the virtual canvas |

## 📂 Project Structure

```text
AI-Virtual-Painter/
│
├── ai_virtual_painter.py
└── README.md
```

## ⚙️ Installation

### Step 1: Install Python

Python 3.11 is recommended for this project because it works well with the MediaPipe version used in the program.

Check the installed Python version:

```bash
python --version
```

To check Python 3.11 specifically, use:

```bash
py -3.11 --version
```

### Step 2: Install Required Libraries

Open Command Prompt or the VS Code terminal and run:

```bash
py -3.11 -m pip install opencv-python mediapipe==0.10.14 numpy
```

## ▶️ How to Run the Project

Open the project folder in Command Prompt or VS Code.

Run the Python file using:

```bash
py -3.11 ai_virtual_painter.py
```

After running the program, the webcam window will open automatically.

## 🎮 Controls

| Action | Control |
|---|---|
| Draw | Raise only the index finger |
| Erase | Raise the index and middle fingers |
| Clear the canvas | Press `C` |
| Exit the program | Press `Q` |

## 🖐️ How the Project Works

The project works through the following steps:

1. The webcam captures live video.
2. OpenCV reads and processes each video frame.
3. MediaPipe detects the user's hand.
4. The program identifies important hand landmark points.
5. The index finger position is used as the brush position.
6. OpenCV draws a line between the previous and current finger positions.
7. The drawing is stored on a virtual canvas.
8. The virtual canvas is displayed over the live camera feed.
9. Raising two fingers activates the eraser.
10. Pressing `C` clears the complete canvas.
11. Pressing `Q` closes the program.

## 📍 Finger Landmarks Used

MediaPipe assigns numbers to different points on the hand. This project uses the following landmarks:

| Finger Point | Landmark ID |
|---|---:|
| Index finger tip | 8 |
| Index finger joint | 6 |
| Middle finger tip | 12 |
| Middle finger joint | 10 |

The program compares these points to identify whether the fingers are raised or lowered.

### Drawing Condition

Drawing starts when the index finger is raised and the middle finger is lowered.

### Erasing Condition

Erasing starts when both the index finger and middle finger are raised.

## 📸 Example Output

When the program starts, the webcam opens and displays the live camera feed.

The user can raise the index finger to draw on the screen. The drawing appears as a coloured line and follows the movement of the finger.

When the index and middle fingers are raised together, the eraser removes the drawing from the selected area. The `C` key clears the complete canvas, and the `Q` key closes the application.

The final output is a live webcam window with a virtual drawing canvas displayed over the camera feed.

## ⚠️ Requirements

The project requires a computer with Python 3.11, a working webcam, and the necessary Python libraries.

A well-lit environment helps MediaPipe detect the hand more accurately. The hand should remain visible inside the webcam frame. A clear background can also improve the tracking performance.

The required libraries are:

- OpenCV
- MediaPipe
- NumPy

## 🛠️ Possible Improvements

The current version provides drawing and erasing through hand gestures. The project can be improved further by adding more interactive features.

Possible future improvements include:

- 🎨 Selecting different colours using hand gestures
- 🖌️ Changing the brush size
- 🧽 Improving the eraser tool
- 🖼️ Saving drawings as image files
- ↩️ Adding undo and redo options
- 🧠 Recognising basic shapes
- 🖥️ Supporting virtual mouse functionality
- 📱 Supporting multiple hands
- 🗂️ Adding a drawing tools menu
- 🌈 Adding different brush colours

These improvements can make the application more flexible and useful for digital drawing and educational activities.

## 🐞 Troubleshooting

### Webcam Not Opening

The webcam may not open if another application is already using it or if camera permission is disabled.

Check the webcam connection and close other applications that may be using the camera. Make sure camera access is enabled in Windows settings.

If required, the webcam command can be changed to:

```python
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
```

### MediaPipe Installation Error

MediaPipe must be installed using a compatible Python version. This project uses Python 3.11.

Install MediaPipe using:

```bash
py -3.11 -m pip install mediapipe==0.10.14
```

Make sure the program is being run with Python 3.11.

### OpenCV or NumPy Error

If OpenCV or NumPy is missing, install them using:

```bash
py -3.11 -m pip install opencv-python numpy
```

### Black Screen Issue

A black screen may appear because of camera permissions, an incorrect camera number, or another application using the webcam.

Check the following:

- The webcam is connected properly.
- Camera permission is enabled.
- Other camera applications are closed.
- The correct camera number is being used.
- The program is restarted after making changes.

### Drawing Is Not Accurate

Hand tracking may become less accurate when the hand is not clearly visible.

For better results:

- Use sufficient lighting.
- Keep the hand inside the camera frame.
- Avoid very fast movements.
- Keep the fingers visible.
- Use a simple background.
- Maintain a suitable distance from the webcam.

## 📚 Learning Outcomes

Developing this project helped me understand the practical use of computer vision and artificial intelligence.

The main concepts learned from this project are:

- Accessing a webcam using OpenCV
- Processing live video frames
- Detecting hands using MediaPipe
- Tracking finger landmark positions
- Recognising simple hand gestures
- Drawing on a virtual canvas
- Using NumPy for image handling
- Combining multiple Python libraries
- Creating a real-time interactive application
- Solving installation and compatibility issues

This project helped me understand how hand gestures can be used as an alternative method of computer interaction.

## 🎯 Use Cases

The AI Virtual Painter can be used in different situations, such as:

- 🖼️ Digital drawing
- 🧑‍🏫 Virtual classroom whiteboards
- 📚 Educational demonstrations
- 🖥️ Touchless computer interaction
- 🎨 Gesture-based painting
- 🤖 Artificial intelligence demonstrations
- 👨‍💻 Computer vision learning
- 🧪 Real-time hand tracking experiments

## 🔍 Core Concepts Used

- Computer Vision
- Hand Gesture Recognition
- Image Processing
- Real-Time Video Processing
- Hand Landmark Detection
- Virtual Canvas Creation
- Human-Computer Interaction
- Bitwise Image Operations

## 👨‍💻 Author

**Name:** Your Name  
**Course:** Computer Science / Artificial Intelligence  
**Project:** AI Virtual Painter  
**Programming Language:** Python  
**Technologies Used:** OpenCV, MediaPipe, NumPy  
**Project Type:** Computer Vision and Artificial Intelligence  

This project was developed as part of my learning experience in Python, artificial intelligence, and computer vision.

## 📜 License

This project was created for educational purposes.

You are free to study, modify, and improve the code.
