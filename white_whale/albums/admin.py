from django.contrib import admin
from .models import Album, UploadedFile

admin.site.register(Album)
admin.site.register(UploadedFile)
