from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

  
    path('convert-image/', views.convert_image, name='convert_image'),
    path('convert-audio/', views.convert_audio, name='convert_audio'),
    path('video-to-audio/', views.video_to_audio, name='video_to_audio'),
    path('resize-image/', views.resize_image, name='resize_image'),
    path('download-youtube/', views.download_youtube, name='download_youtube'),
]