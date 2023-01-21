from django.urls import path
from volumes.views import VolumesView, VolumeView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    path('', VolumesView.as_view(), name='volumes'),
    path('volume/<int:pk>/', VolumeView.as_view(), name='volume'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)