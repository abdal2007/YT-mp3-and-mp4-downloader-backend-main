from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from .utils import get_video_formats, download_video
# Create your views here.


def index(request):
    context = {}

    if request.method == "POST":
        url = request.POST.get("youtube_url")

        if "get_formats" in request.POST:
            # Step 1: Fetch qualities
            # get_formats
            context["formats"] = [f["resolution"] for f in get_video_formats(url)]

            context["url"] = url

        elif "download" in request.POST:
            # Step 2: Download selected quality
            url = request.POST.get("url")
            format_id = request.POST.get("format_id")  # this is now resolution string

            try:
                video_file = download_video(url, format_id)
                return FileResponse(
                    open(video_file, "rb"),
                    as_attachment=True,
                    filename=video_file.name
                )
            except Exception as e:
                return HttpResponse(f"Error: {e}")

    return render(request, "videodl/index.html", context)
            
