# AttendAI Backend

Flask-based REST API backend for **AttendAI** — a smart classroom attendance monitoring system powered by Face Recognition, Raspberry Pi 5, and IoT integration.

This backend handles:

- Face recognition processing
- Attendance recording
- Student management
- System status monitoring
- Hardware communication (Arduino, RGB LED, Buzzer)

---

## Project Overview

AttendAI is an AI + IoT-based classroom attendance system that automates student attendance using facial recognition.

This repository contains the **Flask REST API** running on a Raspberry Pi 5, responsible for:

- Processing camera input
- Matching faces using encodings
- Updating attendance records in SQLite
- Serving real-time data to the frontend dashboard
- Controlling hardware feedback components

---

## 🏗️ System Architecture

Camera  
⬇  
Raspberry Pi 5  
⬇  
Face Recognition Engine (Python + OpenCV)  
⬇  
Flask REST API  
⬇  
Next.js Dashboard (Frontend)  

---

## ⚙️ Tech Stack

- **Python 3**
- **Flask**
- **Flask-CORS**
- **OpenCV**
- **face_recognition**
- **SQLite**
- **Raspberry Pi 5**
- **Arduino (RGB LED + Buzzer integration)**

---

## API Endpoints

### System Status
GET /api/status


Returns:
{
"success": true,
"data": {
"recognition_running": true,
"camera_connected": true,
"present_today": 28,
"total_students": 30
}
}


---

### 👨Students
GET /api/students
POST /api/students


---

### Attendance Records
GET /api/attendance


---

### Control Recognition
POST /api/start
POST /api/stop


---

## Setup & Installation

### 1️⃣ Clone Repository

git clone https://github.com/ryze-7/attend-ai-backend.git
cd attend-ai-backend


---

### 2️⃣ Create Virtual Environment

python3 -m venv venv
source venv/bin/activate


---

### 3️⃣ Install Dependencies

pip install -r requirements.txt


---

### 4️⃣ Run API Server

python3 api.py


Server runs on:

http://0.0.0.0:5000


---

## 🌐 Remote Access (Optional)

To expose API publicly:

ngrok http 5000


Use generated HTTPS URL in frontend environment variable:

NEXT_PUBLIC_API_URL=https://your-ngrok-url.ngrok-free.dev


---

## 🔐 Security Notes

- Designed for local network deployment
- Uses CORS for frontend communication
- No authentication implemented (development version)
- Recommended to add token-based authentication for production

---

## 🧩 Hardware Integration

- Arduino connected via USB
- RGB LED for attendance status
- Passive buzzer for confirmation sound
- Face detection triggers hardware signals

---

## 🚀 Features

✔ Automated attendance using facial recognition  
✔ Real-time dashboard integration  
✔ SQLite-based local database  
✔ IoT hardware feedback system  
✔ RESTful API architecture  
✔ Edge computing (No cloud dependency)  

---

## 🛠 Future Improvements

- JWT authentication
- Cloud deployment (AWS / VPS)
- Multi-class support
- Face training from dashboard
- Email/SMS notifications
- Docker containerization

---
