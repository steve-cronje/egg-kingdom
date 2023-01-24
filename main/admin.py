from django.contrib import admin
from main.models import Ovum
# Register your models here.


class OvumAdmin(admin.ModelAdmin):

    model = Ovum
    list_display = ['user', 'status', 'eggs']

admin.site.register(Ovum, OvumAdmin)