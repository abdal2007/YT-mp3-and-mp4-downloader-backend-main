import yt_dlp
from pathlib import Path
from django.conf import settings
import os

MEDIA_DIR = Path(settings.MEDIA_ROOT)
MEDIA_DIR.mkdir(parents=True, exist_ok=True)

def get_video_formats(url: str):
    """Returns available MP4 qualities."""
    ydl_opts = {"quiet": True}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    formats = []
    seen_res = set()  # Track unique resolutions

    for f in info.get("formats", []):
        if f.get("ext") == "mp4" and f.get("height"):
            res = f['height']
            if res not in seen_res:
                seen_res.add(res)
                formats.append({
                    "format_id": f["format_id"],
                    "resolution": f"{res}p",
                    "fps": f.get("fps"),
                    "filesize": f.get("filesize")
                })
    # Sort by resolution ascending
    formats.sort(key=lambda x: int(x["resolution"].replace("p", "")))
    return formats

def download_video(url: str, resolution: str) -> Path:
    """Downloads selected MP4 quality."""

    ydl_opts = {
        "format": f"bestvideo[height={resolution.replace('p','')}]+bestaudio/best",
        "outtmpl": str(MEDIA_DIR / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "merge_output_format": "mp4",  # Merge video+audio
        "socket_timeout": 15,
        "retries": 10,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        # If merged, extension might change to mp4
        base, ext = os.path.splitext(filename)
        mp4_file = Path(base + ".mp4")
        return mp4_file      

