from django.db import models

class Genre(models.Model):

    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre


class Publisher(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Developer(models.Model):
    
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Game(models.Model):

    name = models.CharField(max_length=100)
    game_bio = models.TextField(max_length=1000, blank=True)
    my_description = models.TextField(max_length=2000, null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    favourite = models.BooleanField(default=False)
    release_date = models.DateField(blank=True)
    published_by = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    developed_by = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
        
