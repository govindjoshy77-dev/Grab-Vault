from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
from moviepy import VideoFileClip, AudioFileClip
import os
import uuid
import yt_dlp

# ✅ Ensure media folder exists
if not os.path.exists("media"):
    os.makedirs("media")

# ✅ FFmpeg path (MoviePy)
os.environ["IMAGEIO_FFMPEG_EXE"] = r"C:\Users\ASUS\Downloads\ffmpeg-8.1\bin\ffmpeg.exe"

# ✅ FFmpeg folder for yt-dlp
FFMPEG_PATH = r"C:\Users\ASUS\Downloads\ffmpeg-8.1\bin"


# 🏠 HOME
def home(request):
    return render(request, 'main/home.html')


# 📊 DASHBOARD
def dashboard(request):
    return render(request, 'main/dashboard.html')


# 🖼 IMAGE CONVERTER
def convert_image(request):
    if request.method == "POST":
        try:
            file = request.FILES['file']
            fmt = request.POST['format']

            img = Image.open(file).convert("RGB")

            filename = str(uuid.uuid4())
            output_path = f"media/{filename}.{fmt}"

            img.save(output_path)
            img.close()

            with open(output_path, "rb") as f:
                response = HttpResponse(f.read(), content_type=f"image/{fmt}")
                response['Content-Disposition'] = f'attachment; filename="converted.{fmt}"'

            os.remove(output_path)
            return response

        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")

    return HttpResponse("Invalid request")


# 🎵 AUDIO CONVERTER
def convert_audio(request):
    if request.method == "POST":
        try:
            file = request.FILES['file']
            fmt = request.POST['format']

            filename = str(uuid.uuid4())

            input_path = f"media/{filename}_input.mp3"
            output_path = f"media/{filename}_output.{fmt}"

            with open(input_path, "wb+") as f:
                for chunk in file.chunks():
                    f.write(chunk)

            audio = AudioFileClip(input_path)
            audio.write_audiofile(output_path)
            audio.close()

            with open(output_path, "rb") as f:
                response = HttpResponse(f.read(), content_type=f"audio/{fmt}")
                response['Content-Disposition'] = f'attachment; filename="converted.{fmt}"'

            os.remove(input_path)
            os.remove(output_path)

            return response

        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")

    return HttpResponse("Invalid request")


# 🎬 VIDEO → AUDIO
def video_to_audio(request):
    if request.method == "POST":
        try:
            file = request.FILES['file']
            fmt = request.POST['format']

            filename = str(uuid.uuid4())

            input_path = f"media/{filename}_video.mp4"
            output_path = f"media/{filename}_audio.{fmt}"

            with open(input_path, "wb+") as f:
                for chunk in file.chunks():
                    f.write(chunk)

            video = VideoFileClip(input_path)
            audio = video.audio
            audio.write_audiofile(output_path)

            audio.close()
            video.close()

            with open(output_path, "rb") as f:
                response = HttpResponse(f.read(), content_type=f"audio/{fmt}")
                response['Content-Disposition'] = f'attachment; filename="audio.{fmt}"'

            os.remove(input_path)
            os.remove(output_path)

            return response

        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")

    return HttpResponse("Invalid request")


# 📐 IMAGE RESIZER
def resize_image(request):
    if request.method == "POST":
        try:
            file = request.FILES['file']
            width = request.POST.get('width')
            height = request.POST.get('height')
            size = request.POST.get('size')
            size_unit = request.POST.get('size_unit')

            img = Image.open(file).convert("RGB")

            if width or height:
                width = int(width) if width else img.width
                height = int(height) if height else img.height
                img = img.resize((width, height))

            filename = str(uuid.uuid4())
            output_path = f"media/{filename}.jpg"

            img.save(output_path, format="JPEG", quality=95)

            # 🔥 Compression logic
            if size:
                target_size = int(size)
                if size_unit == "mb":
                    target_size *= 1024

                quality = 95
                while True:
                    img.save(output_path, format="JPEG", quality=quality)
                    current_size = os.path.getsize(output_path) / 1024

                    if current_size <= target_size or quality <= 10:
                        break
                    quality -= 5

            img.close()

            with open(output_path, "rb") as f:
                response = HttpResponse(f.read(), content_type="image/jpeg")
                response['Content-Disposition'] = 'attachment; filename="resized.jpg"'

            os.remove(output_path)
            return response

        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")

    return HttpResponse("Invalid request")


# 🎥 YOUTUBE DOWNLOADER (FIXED)
def download_youtube(request):
    if request.method == "POST":
        try:
            url = request.POST.get("url")
            fmt = request.POST.get("format")

            print("YT DOWNLOAD HIT:", url, fmt)

            filename = str(uuid.uuid4())

            ydl_opts = {
                'format': 'bestvideo+bestaudio/best' if fmt == "mp4" else 'bestaudio/best',
                'outtmpl': f"media/{filename}.%(ext)s",
                'quiet': False,
                'ffmpeg_location': FFMPEG_PATH,
            }

            # 🎧 MP3 conversion
            if fmt == "mp3":
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            # ✅ Find downloaded file
            output_path = None
            for file in os.listdir("media"):
                if file.startswith(filename):
                    output_path = os.path.join("media", file)
                    break

            if not output_path:
                return HttpResponse("Error: File not found after download")

            # ✅ Send file
            with open(output_path, "rb") as f:
                content_type = "video/mp4" if fmt == "mp4" else "audio/mpeg"
                response = HttpResponse(f.read(), content_type=content_type)
                response['Content-Disposition'] = f'attachment; filename="download.{fmt}"'

            os.remove(output_path)
            return response

        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")

    return HttpResponse("Invalid request")