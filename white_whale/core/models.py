from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation


class Timestamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(Timestamps):
    location = models.CharField(max_length=200, blank=True)
    statement = models.CharField(max_length=250, blank=True)
    status = models.CharField(max_length=1000, blank=True)
    website = models.CharField(max_length=500, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    profile_image = models.ForeignKey(
        'ww_albums.UploadedFile',
        related_name="%(app_label)s_%(class)s_profile_image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    header_image = models.ForeignKey(
        'ww_albums.UploadedFile',
        related_name="%(app_label)s_%(class)s_header_image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    class Meta:
        abstract = True


class User(AbstractUser, Profile, Timestamps):
    middle_name = models.CharField(max_length=150, blank=True)
    birthday = models.DateField(null=True, blank=True)
    comments = GenericRelation('ww_comments.Comment')
    notifications = GenericRelation('ww_notifications.Notification')

    def __str__(self):
        return f'{self.id} - {self.username}'


class AdminNotification(Timestamps):
    admin = models.ForeignKey(
        User,
        related_name='admin',
        null=True,
        on_delete=models.SET_NULL)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    message = models.CharField(max_length=5000)

    def __str__(self):
        return f'{self.id} - {self.user.id}'


class FeatureRequest(Timestamps):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000, blank=True)
    comments = GenericRelation('ww_comments.Comment')
    likes = GenericRelation('ww_likes.Like')

    def __str__(self):
        return f'{self.id} - {self.name}'
