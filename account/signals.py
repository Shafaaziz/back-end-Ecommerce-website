from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        User.objects.create(username=instance)
        print('Profile Created!')

post_save.connect(create_profile,sender=User)

@receiver(post_save, sender=User)
def update_profile(sender,instance,created,**kwargs):
    if created:
        instance.objects.save()
        print('Profile Updated!')

post_save.connect(update_profile,sender=User)