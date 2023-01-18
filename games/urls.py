from django.urls import path
from games.views import ( 
    GamesView, 
    CallApiView, 
    GameDisplayView, 
    GameAddView, 
    GameEditView, 
    game_favourite_update_view,
    GameDeleteView,
)
urlpatterns = [
    path('', GamesView.as_view(), name='games'),
    # path('callapi/', CallApiView.as_view(), name='games-apicall'),
    path('game/<int:pk>/', GameDisplayView.as_view(), name='game'),
    path('add/', GameAddView.as_view(), name='game-add'),
    path('edit/<int:pk>/', GameEditView.as_view(), name='game-edit'),
    path('edit/fave/<int:pk>/', game_favourite_update_view, name='game-fave-edit'),
    path('delete/<int:pk>/', GameDeleteView.as_view(), name='game-delete'),
]