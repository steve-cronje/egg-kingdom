from django.urls import path
from main.views import HomepageView, OvumDetailView

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('ovum/<int:pk>', OvumDetailView.as_view(), name='ovum')
]