from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from white_whale.core.models import Profile, Timestamps, User
from white_whale.comments.models import Comment

class Group(Profile, Timestamps):
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=500)
    email = models.EmailField(blank=True)
    comments = GenericRelation(Comment)

    def __str__(self):
        return f'{self.id} - {self.name}'


class GroupMember(Timestamps):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.group.id}'
