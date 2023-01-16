from django.urls import path
from games.views import GamesShelvesView, CallApiView, GameDisplayView, GameAddView, GameEditView

urlpatterns = [
    path('shelves/', GamesShelvesView.as_view(), name='games-shelves'),
    path('callapi/', CallApiView.as_view(), name='games-apicall'),
    path('game/<str:pk>/', GameDisplayView.as_view(), name='game-display'),
    path('add/', GameAddView.as_view(), name='game-add'),
    path('edit/<str:pk>/', GameEditView.as_view(), name='game-edit')
]