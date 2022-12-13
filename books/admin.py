from django.contrib import admin
from books.models import Author, Genre, Book

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):

    model = Author
    list_display = ['name']
    search_fields = ['name']

class GenreAdmin(admin.ModelAdmin):

    model = Genre
    list_display = ['name']
    search_fields = ['name']

class BookAdmin(admin.ModelAdmin):

    model = Book
    list_display = ['name', 'type', 'read', 'author']
    search_fields = ['name']
    list_filter = ['read', 'type']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)