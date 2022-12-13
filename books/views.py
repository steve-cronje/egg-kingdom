from django.shortcuts import render
from django.views.generic import ListView
from books.models import Book

# Create your views here.
class BookShelvesView(ListView):

    model = Book
    template_name = 'books/shelves.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['my_books'] = self.model.objects.all()
        return context