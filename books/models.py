from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):

    READ = 'HR'
    READING = 'CR'
    NOT_READ = 'NR'
    READ_STATUS = [
        (READ, "Have read"),
        (READING, 'Currently reading'),
        (NOT_READ, 'Have not read')
    ]

    NOVEL = 'NOVEL'
    BIOGRAPHY = 'BIO'
    AUTOBIOGRAPHY = 'ABIO'
    MANGA = 'MANGA'
    SHORT_STORY = 'SHORT'
    BOOK_TYPE = [
        (NOVEL, 'Novel'),
        (BIOGRAPHY, 'Biography'),
        (AUTOBIOGRAPHY, 'Auto-biography'),
        (MANGA, 'Manga'),
        (SHORT_STORY, 'Short story')
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(choices=BOOK_TYPE, max_length=5, default=NOVEL)
    read = models.CharField(choices=READ_STATUS, max_length=2, default=READ)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre)
    bio = models.TextField(blank=True, null=True)
    my_description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name