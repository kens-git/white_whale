from django.urls import path
from rest_framework import routers
from .views import AdminNotificationViewSet, FeatureRequestViewSet, UserViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'admin-notifications', AdminNotificationViewSet)
router.register(r'feature-request', FeatureRequestViewSet)
urlpatterns = router.urls
