from hashlib import md5
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from graphql import GraphQLError
from django.db import models
from applications.models import Application

class URL(models.Model):
    application = models.ForeignKey(Application , on_delete = models.CASCADE , null = True )
    full_url = models.URLField(unique=True)
    url_hash = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]
        validate = URLValidator()
        try:
            validate(self.full_url)
        except ValidationError as e:
            raise GraphQLError('inavlid url')
        return super().save(*args, **kwargs)
