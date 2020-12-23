from django.db import models
import uuid

# Create your models here.


class NotificationUser(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    fcmkey = models.TextField()
    device_id = models.CharField(max_length=100, default='deviceid')
    device_name = models.CharField(max_length=100,default='devicename')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Notification(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid.uuid4 , editable=False)
    title = models.CharField(max_length=250)
    users = models.ManyToManyField("notifications.NotificationUser", related_name='users')
    body = models.TextField()
    extra = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

