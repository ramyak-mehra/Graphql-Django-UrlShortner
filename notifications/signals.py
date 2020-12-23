from .models import Notification , NotificationUser
from .utils import send_firebase_notifications
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save , model=Notification)
def send_messages(sender , instance , created , **kwargs):
    if created:
        if instance.extra:
            send_firebase_notifications(instance.users , title=instance.title , body=instance.body , extra=instance.extra )
        else:
            send_firebase_notifications(instance.users , title=instance.title , body=instance.body)