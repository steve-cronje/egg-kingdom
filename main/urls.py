from django.urls import path
from main.views import HomepageView, VolumesView, VolumeView, MusicShelvesView


urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('volumes/', VolumesView.as_view(), name='volumes'),
    path('volumes/volume/<int:volumenum>/', VolumeView.as_view(), name='volume'),
    path('music/shelves/', MusicShelvesView.as_view(), name='music-shelves'),
]