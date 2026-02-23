import os
from pathlib import Path
import yt_dlp
from django.conf import settings
import subprocess

# Ensure MEDIA_ROOT exists
MEDIA_DIR = Path(settings.MEDIA_ROOT)
#if media root does not exist then make a new one
MEDIA_DIR.mkdir(parents=True, exist_ok=True)

def download_best_audio(url: str) -> Path:
    """Download best audio only (no mp3 conversion yet)."""
    
    ydl_opts = {
        "format": "bestaudio/best",#download in best audio
        "outtmpl": str(MEDIA_DIR / "%(title)s.%(ext)s"),# set file name same as the title
        "noplaylist": True, # if user provide url of a playlist then download only video not the whole playlist
        "prefer_ffmpeg": True,# use ffmpeg for converstion and download
        
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)# extract information like title duration etc.
        filename = ydl.prepare_filename(info)
        
        return Path(filename)
    

def convert_to_multiple_mp3(input_file: Path) -> dict:
    """Create 5 MP3 qualities and return dict of files."""

    qualities = {
        "64": "64k",
        "128": "128k",
        "192": "192k",
        "256": "256k",
        "320": "320k",
    }

    output_files = {}

    for q, bitrate in qualities.items():
        out_path = input_file.with_name(f"{input_file.stem}_{q}.mp3")

        subprocess.run([
            "ffmpeg", "-i", str(input_file),
            "-b:a", bitrate,
            str(out_path),
            "-y"
        ])

        output_files[q] = out_path.name

    return output_files    
