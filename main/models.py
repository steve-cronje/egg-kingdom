from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Ovum(models.Model):

    CITIZEN = 'citizen'
    NOBILITY = 'nobility'
    ROYALTY = 'royalty'
    BOSSMAN = 'bossman'
    STATUS = [
        (CITIZEN, 'Civis Ovum'),
        (NOBILITY, 'Ovum Princeps'),
        (ROYALTY, 'Ovum Regem'),
        (BOSSMAN, 'Dominus Omnium Ova')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    status = models.CharField(max_length=8, choices=STATUS, default=CITIZEN)
    eggs = models.IntegerField(default=10)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='users/images/')

    def __str__(self):
        return self.status+" | "+self.user.username

    def get_absolute_url(self):
        return reverse('ovum', kwargs={'pk', self.user.pk})
