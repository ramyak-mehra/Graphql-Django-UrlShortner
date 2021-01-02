import enum
from push_notifications.models import APNSDevice, GCMDevice
from django.core import mail
from django.template.loader import render_to_string
from .models import Notification , NotificationUser
from django.conf import settings 


class NotificationType(enum.Enum):
    NewQuestion = "New Question was uploaded to "
    NewReply = "New Reply on your question "
    NewLike = "New Like"


def send_firebase_notifications(users , title , body , extra=None):
    for user in users:
        if user.gcmdevice_set.exists():
            user_devices = user.gcmdevice_set.all()
            if extra:
                user_devices.send_message(body, title = title ,extra=extra)
            else:
                user_devices.send_message(body, title = title)


def send_email(users, title, subject,  body, extra=None):
    connection = mail.get_connection()
    email_list = []
    for user in users:
        email = mail.EmailMessage(
            subject,
            render_to_string('notifications/email.html', {
                'user': user.username,
                'body': body
            }),
            settings.EMAIL_HOST_USER,
            [user],
            connection=connection,
        )
        email_list.append(email)

    connection.send_messages(email_list)

    # connection = mail.get_connection()
    # email = mail.EmailMessage(
    #     subject,
    #     render_to_string('notifications/email.html', {
    #         'user': 'sanchit',
    #         'body': body
    #     }),
    #     settings.EMAIL_HOST_USER,
    #     users,
    #     connection=connection,
    # )

    # connection.send_messages(email)