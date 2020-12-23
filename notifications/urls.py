from .views import NotificationAPIView
from django.urls import path, include


urlpatterns = [
    path('notifications/'  , NotificationAPIView.as_view()),
]
