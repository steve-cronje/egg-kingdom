from django.urls import path
from books.views import BookShelvesView

urlpatterns = [
    path('shelves/', BookShelvesView.as_view(), name='book-shelves'),
]