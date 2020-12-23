from rest_framework import serializers
from .models import NotificationUser , Notification
from push_notifications.models import GCMDevice

class NotificationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationUser
        fields = '__all__'

class NotificationUserRelatedField(serializers.RelatedField):
    def get_queryset(self):
        return NotificationUser.objects.all()
    def to_internal_value(self , data):
        user , created = NotificationUser.objects.get_or_create(username = data['username'] , fcmkey = data['fcmkey'] , 
                                                        email = data['email'],first_name = data['first_name'] ,
                                                         last_name = data['last_name'])
        if created:
            fcm_device , created = GCMDevice.objects.get_or_create(registration_id=user.fcmkey , name=user.device_name ,device_id=user.device_id , cloud_message_type="FCM" , user=user)
        return user
    def to_representation(self, value):
        serializer = NotificationUserSerializer(value)
        return serializer.data
class NotificationSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    body = serializers.CharField(required=False)
    extra = serializers.JSONField()
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')
    userList = NotificationUserRelatedField(many=True , required=False , source='users')

    class Meta:
        model = Notification
        fields = (
            'title',
            'body',
            'extra',
            'createdAt',
            'updatedAt',
            'userList'
        )
    def create(self , validated_data):
        title = validated_data['title']
        body = validated_data['body']
        extra = validated_data['extra']
        users = validated_data['users']
        print(validated_data)
        notification = Notification.objects.create(title=title , body=body , extra=extra)
        if users is not None:
            for user in users:
                notification.users.add(user.pk)
        return notification
    def get_created_at(self , instance):
        return instance.created_at.isoformat()

    def get_updated_at(self, instance):
        return instance.updated_at.isoformat() 


