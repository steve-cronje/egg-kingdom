from django.urls import path
from games.views import GamesShelvesView

urlpatterns = [
    path('shelves/', GamesShelvesView.as_view(), name='games-shelves'),
]