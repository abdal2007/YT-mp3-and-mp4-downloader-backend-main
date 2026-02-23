from django.http import JsonResponse, FileResponse, HttpResponse
from downloader.utils import download_best_audio, convert_to_multiple_mp3
from django.conf import settings
from pathlib import Path
from django.views.decorators.csrf import csrf_exempt

# --MP3 FORMATS(GET API)--
def mp3_formats(request):
    print("API called")
    try:
        url = request.GET.get("url")
        if not url:
            return JsonResponse({"error": "URL is required"}, status=400)
        print("Downloading audio from:", url)
        audio_file = download_best_audio(url)
        print("Downloaded file:", audio_file)

        qualities = convert_to_multiple_mp3(audio_file)
        print("Available qualities:", qualities)

        return JsonResponse({"qualities": qualities})

    except Exception as e:
        print("Error occurred:", e)
        return JsonResponse({"error": str(e)}, status=500)

# --MP3 DOWNLOAD(POST API)--
@csrf_exempt
def mp3_download(request):
    try:
        file_name = request.POST.get("file_name")
        if not file_name:
            return JsonResponse({"error": "file_name is required"}, status=400)

        file_path = Path(settings.MEDIA_ROOT) / file_name

        return FileResponse(
            open(file_path, "rb"),
            as_attachment=True,
            filename=file_name
        )

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
