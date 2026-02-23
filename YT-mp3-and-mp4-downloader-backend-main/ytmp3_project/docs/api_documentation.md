# 📘 YouTube MP3 & MP4 Converter — API Documentation

This document explains all available API endpoints, required parameters, expected responses, and how to test each API using Thunder Client or Postman.

---

# 🔗 Base URL

```
http://127.0.0.1:8000/api/
```

---

#  MP3 API Endpoints

---

## 1️⃣ Get MP3 Formats

Fetch all available audio qualities for a given YouTube URL.

### **Endpoint**

```
GET /api/mp3/formats/?url=YOUTUBE_URL
```

### **Query Parameter**

| Name | Type   | Required | Description        |
| ---- | ------ | -------- | ------------------ |
| url  | string | yes      | YouTube video link |

### **Example Request**

```
GET /api/mp3/formats/?url=https://youtu.be/VIDEO_ID
```

### **Success Response**

```json
{
  "qualities": [
    "video-title-128kbps.mp3",
    "video-title-192kbps.mp3",
    "video-title-256kbps.mp3"
  ]
}
```

### **Error Response**

```json
{
  "error": "URL is required"
}
```

---

## 2️⃣ Download MP3

Downloads the selected MP3 file.

### **Endpoint**

```
POST /api/mp3/download/
```

### **Body (JSON)**

| Field     | Type   | Required | Description                        |
| --------- | ------ | -------- | ---------------------------------- |
| file_name | string | yes      | MP3 file name returned from step 1 |

### **Example Body**

```json
{
  "file_name": "video-title-128kbps.mp3"
}
```

### **Response**

* Returns the MP3 file as an attachment.

---

#  MP4 API Endpoints

---

## 3️⃣ Get MP4 Formats

Fetch available MP4 formats (resolution + fps + file size).

### **Endpoint**

```
GET /api/mp4/formats/?url=YOUTUBE_URL
```

### **Query Param**

| Name | Type   | Required |
| ---- | ------ | -------- |
| url  | string | yes      |

### **Example Response**

```json
{
  "formats": [
    {
      "format_id": "93",
      "resolution": "360p",
      "fps": 30,
      "filesize": 3200000
    }
  ]
}
```

---

## 4️⃣ Download MP4

Download a video by providing its URL + desired resolution.

### **Endpoint**

```
POST /api/mp4/download/
```

### **Body (JSON)**

| Field      | Type   | Required | Description                                         |
| ---------- | ------ | -------- | --------------------------------------------------- |
| url        | string | yes      | YouTube link                                        |
| resolution | string | yes      | Resolution returned from formats API (e.g., "720p") |

### **Example Body**

```json
{
  "url": "https://youtu.be/VIDEO_ID",
  "resolution": "720p"
}
```

### **Response**

* File download begins.

---

# 🔧 Error Codes

| Code | Meaning                 |
| ---- | ----------------------- |
| 400  | Missing required fields |
| 404  | File not found          |
| 500  | Internal server error   |

Example:

```json
{
  "error": "url and resolution required"
}
```

---

# 🧪 Testing Instructions (Thunder Client / Postman)

---

## ✔ MP3 Test Flow

1. **GET formats**

   ```
   GET /api/mp3/formats/?url=YOUTUBE_URL
   ```
2. Response se **file_name** uthao.
3. **POST download**

   ```
   POST /api/mp3/download/
   ```

   Body:

   ```json
   {
     "file_name": "video-title-128kbps.mp3"
   }
   ```

---

## ✔ MP4 Test Flow

1. **GET formats**

   ```
   GET /api/mp4/formats/?url=YOUTUBE_URL
   ```
2. Response se **resolution** choose karo.
3. **POST download**

   ```json
   {
     "url": "YOUTUBE_URL",
     "resolution": "720p"
   }
   ```

---

# 📁 Project Requirements

* Python 3
* Django
* yt-dlp
* FFmpeg installed
* Media folder auto-created for saving files

---

# 📝 File Storage

All MP3 / MP4 files are saved automatically into:

```
/media/
```

---

# 👨‍💻 Developer Notes

* CSRF disabled recommended for API clients.
* Use Django's dev server only for local testing.
* yt-dlp handles YouTube link extraction & format detection.

---


