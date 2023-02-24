from rest_framework import viewsets
from .models import AdminNotification, FeatureRequest, User
from .serializers import (AdminNotificationSerializer, FeatureRequestSerializer,
                          UserSerializer)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'put', 'patch', 'head', 'options']

class AdminNotificationViewSet(viewsets.ModelViewSet):
    queryset = AdminNotification.objects.all()
    serializer_class = AdminNotificationSerializer
    http_method_names = ['get', 'head', 'options']

class FeatureRequestViewSet(viewsets.ModelViewSet):
    queryset = FeatureRequest.objects.all()
    serializer_class = FeatureRequestSerializer
