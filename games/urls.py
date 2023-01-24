from django.urls import path
from games.views import ( 
    GamesView, 
    GameDisplayView, 
    GameAddView, 
    GameEditView, 
    game_favourite_update_view,
    GameDeleteView,
)
urlpatterns = [
    path('', GamesView.as_view(), name='list'),
    # path('callapi/', CallApiView.as_view(), name='games-apicall'),
    path('game/<int:pk>/', GameDisplayView.as_view(), name='game'),
    path('add/', GameAddView.as_view(), name='add'),
    path('edit/<int:pk>/', GameEditView.as_view(), name='edit'),
    path('edit/fave/<int:pk>/', game_favourite_update_view, name='fave-edit'),
    path('delete/<int:pk>/', GameDeleteView.as_view(), name='delete'),
]