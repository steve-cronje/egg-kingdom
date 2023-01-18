from django.db import models
from django.urls import reverse


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
    release_date = models.DateField(blank=True, null=True)
    companies = models.ManyToManyField(Company)
    cover_url = models.URLField(blank=True, null=True)
    favourite = models.BooleanField(blank=True, null=True)
    abs_favourite = models.BooleanField(blank=True, null=True)
    want = models.BooleanField(blank=True, null=True)

    def make_favourite(self, option: int):
        '''
        updates the favourite status of game
        enter '1' as option for favourite
        enter '2' as option for absolute favourite
        enter '0' as option for want to play
        '''
        if option == 0:
            self.favourite = False
            self.abs_favourite = False
            self.want = True
        elif option == 1:
            self.favourite = True
            self.abs_favourite = False
            self.want = False
        elif option == 2:
            self.favourite = False
            self.abs_favourite = True
            self.want = False
        self.save()
        print(f'{self.name} has had its favourite status updated!')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game', kwargs={'pk' : self.pk})
        
class Screenshot(models.Model):

    id = models.IntegerField(primary_key=True)
    url = models.URLField(blank=True, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.game.name + " : " + self.url
