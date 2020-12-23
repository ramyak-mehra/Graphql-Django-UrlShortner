from django.shortcuts import render
from rest_framework.exceptions import NotFound , PermissionDenied
from rest_framework import mixins, generics , status , viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notification  , NotificationUser
from .serializers import NotificationSerializer , NotificationUserSerializer


class NotificationAPIView(APIView):
    
    def get(self , request):
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications , many=True)
        return Response(serializer.data)

    def post(self , request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

