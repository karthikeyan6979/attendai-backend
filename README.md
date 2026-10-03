# AttendAI Backend

Flask REST API for **AttendAI**, a smart classroom attendance system that uses face recognition, a Raspberry Pi 5, and IoT hardware feedback. It runs entirely on the Pi, with no cloud dependency by default.

The backend:

- Processes camera input and matches faces against stored encodings
- Records attendance in a local SQLite database
- Manages student records
- Reports system status to the frontend dashboard
- Drives hardware feedback (RGB LED and buzzer via Arduino)

The dashboard that consumes this API is a separate Next.js app.

## Features

- Automated attendance through facial recognition
- Real-time data for the dashboard over a REST API
- Local SQLite storage
- Arduino-based feedback: RGB LED for attendance status, passive buzzer for confirmation
- Start and stop recognition remotely through the API
- Runs on the edge, on a Raspberry Pi 5

## Tech stack

| Component | Technology |
|---|---|
| Language | Python 3 |
| API | Flask, Flask-CORS |
| Vision | OpenCV, face_recognition |
| Database | SQLite |
| Hardware | Raspberry Pi 5, Arduino (RGB LED, passive buzzer) |
| Frontend | Next.js (separate repository) |

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/ryze-7/attend-ai-backend.git
cd attend-ai-backend
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

`face_recognition` depends on `dlib`, which can take a long time to build on a Raspberry Pi. Expect the install to be slow.

### 4. Run the server

```bash
python3 api.py
```

The API is served at `http://0.0.0.0:5000`.

## API reference

Base URL: `http://<pi-ip-address>:5000`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/status` | System status and today's attendance summary |
| GET | `/api/students` | List all students |
| POST | `/api/students` | Add a student |
| GET | `/api/attendance` | Get attendance records |
| POST | `/api/start` | Start face recognition |
| POST | `/api/stop` | Stop face recognition |

### Example: `GET /api/status`

```json
{
  "success": true,
  "data": {
    "recognition_running": true,
    "camera_connected": true,
    "present_today": 28,
    "total_students": 30
  }
}
```

## Hardware

- An Arduino is connected to the Raspberry Pi over USB.
- The RGB LED shows attendance status.
- The passive buzzer plays a confirmation sound.
- A successful face detection triggers the LED and buzzer signals.

## Connecting the frontend

For access from outside the local network, you can tunnel the API with ngrok:

```bash
ngrok http 5000
```

Then set the generated HTTPS URL in the frontend's environment:

```
NEXT_PUBLIC_API_URL=https://your-ngrok-url.ngrok-free.dev
```

## Security

This is a development version.

- There is **no authentication**. Anyone who can reach the API can read attendance data, add students, and start or stop recognition.
- CORS only controls which browser origins may call the API. It does not protect it.
- Keep the API on a trusted local network. Use ngrok only for short demos, and shut the tunnel down afterwards.
- Token-based authentication is needed before any real deployment.

## Roadmap

- [ ] JWT authentication
- [ ] Face enrollment from the dashboard
- [ ] Multi-class support
- [ ] Email and SMS notifications
- [ ] Docker containerization
- [ ] Cloud deployment (AWS / VPS)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
