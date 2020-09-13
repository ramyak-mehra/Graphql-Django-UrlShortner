from django.contrib import admin
from .models import URL

class URLAdmin(admin.ModelAdmin):
    pass
admin.site.register(URL , URLAdmin)