from django.db import models
import uuid
# Create your models here.


class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    token = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return f'{self.name}'
