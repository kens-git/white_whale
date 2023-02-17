from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from white_whale.core.models import Timestamps, User

class Comment(Timestamps):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.SET_NULL)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    comment = models.CharField(max_length=5000)

    def __str__(self):
        return f'{self.id} - {self.content_object.id}'
