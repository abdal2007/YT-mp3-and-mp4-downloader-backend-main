from django.http import JsonResponse, FileResponse, HttpResponse
from videodl.utils import get_video_formats, download_video
from pathlib import Path
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# -- MP4 Format(GET API)--
def mp4_formats(request):
    try:
        url = request.GET.get("url")
        if not url:
            return JsonResponse({"error": "URL is required"}, status=400)

        formats = get_video_formats(url)
        return JsonResponse({"formats": formats})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

# --MP4 Download(POST API)--
@csrf_exempt
def mp4_download(request):
    try:
        url = request.POST.get("url")
        resolution = request.POST.get("resolution")

        if not url or not resolution:
            return JsonResponse({"error": "url and resolution required"}, status=400)

        file_path = download_video(url, resolution)

        return FileResponse(
            open(file_path, "rb"),
            as_attachment=True,
            filename=file_path.name
        )

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
