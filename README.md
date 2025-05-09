# Hand-Mouse-Controller

Hand Mouse Controller using MediaPipe

This project enables mouse control using your hand gestures tracked in real-time through a webcam. Leveraging MediaPipe for hand landmark detection, OpenCV for video processing, and PyAutoGUI for mouse control, it creates a virtual interface where your fingers become your mouse.

🚧 Features

✨ Move your cursor by moving your index finger

☑️ Click by bringing your thumb and index finger close together

⏹ Press ESC to exit the application

---



💡 How It Works

Index fingertip (landmark ID 8) controls cursor movement

Thumb tip (landmark ID 4) is used to trigger mouse click when close to the index finger

Distance between thumb and index finger is measured

Click is simulated if distance is below a threshold

---



🔗 Requirements

Python 3.7+

Webcam

---


Move your index finger to move the mouse

Bring your index finger and thumb close to simulate a click

Press ESC to quit

---


👥 Contributing

Contributions are welcome! Please fork the repo and submit a pull request. For major changes, open an issue first to discuss what you'd like to change.

---


✉️ License

MIT — Feel free to use this project for personal or commercial use.

---


👤 Author

Ridham GargThapar Institute of Engineering and Technology, Patiala

Developed with ❤️ using MediaPipe and OpenCV.

