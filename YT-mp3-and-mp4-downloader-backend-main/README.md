# YT-mp3-and-mp4-downloader-backend

## 🎥 Demo Videos

▶️ **MP4 Download Feature**  


https://github.com/user-attachments/assets/88b61205-2537-4909-be3e-83dd58fcbc3d



▶️ **MP3 Download Feature**  


https://github.com/user-attachments/assets/f3efecec-5109-40e4-8482-e92cea1bd5dd



A Django-based REST API system that downloads and converts YouTube videos into **MP3** and **MP4** formats using **yt-dlp** and **FFmpeg**.

---

##  Features

###  MP3
- Fetch available audio qualities.
- Converts audio to multiple MP3 bitrates.
- Direct file downloading through API.

###  MP4
- Fetch available video formats (144p → 1440p).
- Download MP4 using selected resolution.
- Fast & optimized video extraction.

---

##  Tech Stack
- **Python 3**
- **Django**
- **yt-dlp**
- **FFmpeg**
- Thunder Client / Postman (for API testing)

---

# 📁 Project Structure
```
ytmp3_project/
│
├── downloader/
│ ├── utils.py
│ ├── views.py
│ |
│ └── ...
|
|── docs/
|  ├── api_documentation.md
|
|__videodl/
|  ├── utils.py
|  ├── views.py
|  └── ...
├── api/
|  ├── views_mp3.py
|  ├── views_mp4.py
|  └── ...
│
|── ytmp3_project/ #main project
|  ├── settings.py
|  └── ...
|
├── media/
│
├── manage.py
└── requirements.txt
```
# 2️⃣ Create Virtual Environment
```
python -m venv venv
```
# 3️⃣ Activate Virtual Environment
```
venv\Scripts\activate
```
# 4️⃣ Install Requirements
```
pip install -r requirements.txt
```
# 5️⃣ Run Server
```
python manage.py runserver
```
Server will start at:
```
http://127.0.0.1:8000/
```





