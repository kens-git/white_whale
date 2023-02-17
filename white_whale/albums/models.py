from django.db import models
from white_whale.core.models import Timestamps, User

# TODO: move
def user_directory_path(instance, filename: str):
    return f'user{instance.album.user.id}/album{instance.album.id}/{filename}'

class Album(Timestamps):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f'{self.id} - {self.name}'


class UploadedFile(Timestamps):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    file = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return f'{self.id} - {self.name}'
