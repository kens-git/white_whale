from django.db import models
from white_whale.core.models import Timestamps, User

class Message(Timestamps):
    from_user = models.ForeignKey(
        User,
        related_name="from_user",
        on_delete=models.PROTECT)
    to_user = models.ForeignKey(
        User,
        related_name="to_user",
        on_delete=models.PROTECT)
    content = models.CharField(max_length=5000)

    def __str__(self):
        return f'{self.id} - {self.from_user.id}->{self.to_user.id}'
