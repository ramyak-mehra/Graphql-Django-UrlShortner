from hashlib import md5
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.contrib.sites.models import Site
from graphql import GraphQLError
from django.db import models
from applications.models import Application
import uuid


class URL(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    application = models.ForeignKey(
        Application, on_delete=models.CASCADE, null=True)
    full_url = models.URLField(unique=True)
    url_hash = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)
    shortened_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{ self.application } : { self.full_url }'

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]
        current_url = Site.objects.get_current().domain
        self.shortened_url = f'{current_url}/{self.url_hash}'
        validate = URLValidator()

        try:
            validate(self.full_url)
        except ValidationError as e:
            raise GraphQLError('inavlid url')
        return super().save(*args, **kwargs)
