# Hand Gesture Controlled Browser Automation

A real-time hand gesture recognition project built with Python, OpenCV, and MediaPipe that detects hand gestures through webcam input and automatically opens different websites based on the recognized gesture.

### Features
Real-time hand tracking using webcam
Detects multiple hand gestures based on finger positions
Opens specific websites for each recognized gesture
Prevents repeated browser opening for the same gesture
Displays live gesture detection on screen

### Tech Stack
Python
OpenCV
MediaPipe
WebBrowser Module
How It Works

The system tracks hand landmarks using MediaPipe, analyzes finger positions to identify gestures, and maps each gesture to a predefined website. When a new gesture is detected, the corresponding website opens automatically.

### Example Gesture Mapping
L → YouTube,
I → Google,
V → LinkedIn,
E → Gmail,
5 → IRCTC,
Y → Facebook

### Future Improvements
Add support for custom user-defined gestures
Improve gesture recognition accuracy
Add voice feedback for detected gestures
Create GUI for gesture-to-website mapping
