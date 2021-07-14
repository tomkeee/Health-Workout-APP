from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Training

@receiver(post_save,sender=User)
def save_profile(sender,instance,created,**kwargs):
    if created:
        Training.objects.create(account=instance,day="Monday")
        Training.objects.create(account=instance,day="Tuesday")
        Training.objects.create(account=instance,day="Wednesday")
        Training.objects.create(account=instance,day="Thursday")
        Training.objects.create(account=instance,day="Friday")
        Training.objects.create(account=instance,day="Saturday")
        Training.objects.create(account=instance,day="Sunday")
