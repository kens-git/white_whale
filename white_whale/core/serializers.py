from django.conf import settings
from rest_framework import serializers
from .models import AdminNotification, FeatureRequest, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_login', 'username', 'first_name',
                  'last_name', 'email', 'created_at', 'modified_at', 'location',
                  'statement', 'status', 'website', 'phone', 'middle_name', 'birthday',
                  'profile_image', 'header_image']
        read_only_fields = ['username', 'last_login', 'created_at', 'modified_at']

class AdminNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminNotification
        fields = '__all__'

class FeatureRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureRequest
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'modified_at', 'user']
