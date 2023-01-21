from django.db import models
from django.urls import reverse

# Create your models here.

class Meme(models.Model):

    volume = models.IntegerField(primary_key=True, auto_created=True)
    image_url = models.ImageField(upload_to='memes/')

    def __str__(self):
        return f'Volume {self.volume}'

    def get_absolute_url(self):
        return reverse('volume', kwargs={'pk' : self.pk})