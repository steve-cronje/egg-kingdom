from django.contrib import admin
from volumes.models import Meme

# Register your models here.

class MemeAdmin(admin.ModelAdmin):

    model = Meme
    fields = ['volume', 'image_url']
admin.site.register(Meme, MemeAdmin)