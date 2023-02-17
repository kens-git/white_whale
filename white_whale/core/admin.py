from django.contrib import admin
from .models import AdminNotification, FeatureRequest, User

admin.site.register(AdminNotification)
admin.site.register(FeatureRequest)
admin.site.register(User)
