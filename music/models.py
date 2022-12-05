from django.db import models
import datetime

class Playlist(models.Model):

    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)
    spotify_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Artist(models.Model):

    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=100)
    artist_type = models.CharField(max_length=100, blank=True)
    spotify_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Album(models.Model):

    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    album_type = models.CharField(max_length=100, blank=True, null=True)
    artists = models.ManyToManyField(Artist)
    spotify_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    image_url_big = models.URLField(blank=True, null=True)
    release_date = models.DateField(blank=True, auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Track(models.Model):

    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True)
    artists = models.ManyToManyField(Artist)
    playlist = models.ManyToManyField(Playlist)
    spotify_url = models.URLField(blank=True, null=True)
    preview_url = models.URLField(blank=True, null=True)
    explicit_content = models.BooleanField(default=False)
    duration = models.IntegerField(null=True)

    @property
    def get_duration(self):
        duration = str(datetime.timedelta(milliseconds=self.duration))
        if int(duration[0]) > 0:
            if len(duration) > 7:
                return duration[:len(duration)-7:]
            else:
                return duration
        else:
            if len(duration) > 7:
                return duration[2:len(duration)-7:]
            else:
                return duration[2::]


    def __str__(self):
        return self.name

