from django.db import models


class Genre(models.Model):

    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre


class Company(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Game(models.Model):
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    game_bio = models.TextField(max_length=1000, blank=True, null=True)
    my_description = models.TextField(max_length=2000, null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    favourite = models.BooleanField(default=False)
    release_date = models.DateField(blank=True, null=True)
    companies = models.ManyToManyField(Company)
    cover_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
        
class Screenshot(models.Model):

    id = models.IntegerField(primary_key=True)
    url = models.URLField(blank=True, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.game.name + " : " + self.url