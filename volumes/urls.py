from django.urls import path
from volumes.views import VolumesView, VolumeView

urlpatterns = [ 
    path('', VolumesView.as_view(), name='volumes'),
    path('volume/<int:volumenum>/', VolumeView.as_view(), name='volume'),
]