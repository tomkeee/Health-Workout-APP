from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User)
def creat_new_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(account=instance)
