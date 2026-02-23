from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from .utils import download_best_audio, convert_to_multiple_mp3
from django.conf import settings
from pathlib import Path
from django.utils.encoding import smart_str

def index(request):
    # if user submit the form
    if request.method == "POST":
        # If user selected a quality to download
        selected = request.POST.get("quality_select")
        # if user select the quality
        if selected:

            file_path = Path(settings.MEDIA_ROOT) / selected  # now returns Path
            try:
                response = FileResponse(
                        open(file_path, "rb"),
                        as_attachment=True,
                        filename=smart_str(file_path.name)  # ensures proper filename
                    )
                #return FileResponse(open(file_path, "rb"), as_attachment=True, filename=selected)
                return response
            except Exception as e:
                return HttpResponse(f"Error downloading file: {e}", status=500)
        
        # Otherwise user submitted YouTube URL
        url = request.POST.get("youtube_url") 
        if url:
            try:
                # Step 1: Download best audio
                audio_file = download_best_audio(url)

                # Step 2: Convert into 5 qualities
                mp3_versions = convert_to_multiple_mp3(audio_file)

                return render(request, "downloader/index.html", {
                    "qualities": mp3_versions
                })
            except Exception as e:
                return HttpResponse(f"Error: {e}", status=500)
    return render(request, "downloader/index.html")        


                
