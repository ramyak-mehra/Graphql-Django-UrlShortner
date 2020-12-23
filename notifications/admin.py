# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import NotificationUser, Notification


@admin.register(NotificationUser)
class NotificationUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'fcmkey',
        'first_name',
        'last_name',
    )


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'body',
        'extra',
        'created_at',
        'updated_at',
    )
    list_filter = ('created_at', 'updated_at')
    raw_id_fields = ('users',)
    date_hierarchy = 'created_at'