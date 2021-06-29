from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save,sender=User)
def post_save_create_profile(sender,instance,created,**kwargs):
    if created:
        print(instance)
        Profile.objects.create(account=instance)
