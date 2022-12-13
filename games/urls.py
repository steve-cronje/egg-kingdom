from django.urls import path
from games.views import GamesShelvesView, CallApiView, GameDisplayView

urlpatterns = [
    path('shelves/', GamesShelvesView.as_view(), name='games-shelves'),
    path('callapi/', CallApiView.as_view(), name='games-apicall'),
    path('game/<str:pk>/', GameDisplayView.as_view(), name='game-display'),
]