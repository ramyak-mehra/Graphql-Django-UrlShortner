# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import URL


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'is_flagged',
        'application',
        'full_url',
        'url_hash',
        'clicks',
        'shortened_url',
        'created_at',
    )
    list_filter = ('is_flagged', 'application', 'created_at')
    date_hierarchy = 'created_at'
