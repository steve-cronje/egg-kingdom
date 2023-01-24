from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import Ovum
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def create_ovum(sender, instance, created, **kwargs):

    if created:
        ova = Ovum.objects.create(user=instance)