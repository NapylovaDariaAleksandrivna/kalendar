from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid


class Task(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4)
    tag = models.CharField(max_length=120)
    text = models.TextField()
    to_date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        db_table = 'tasks'
        ordering = ['to_date']
        

from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        default='profile_avatars/avatar.png', # default avatar
        upload_to='profile_avatars' # dir to store the image
    )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.avatar.path)
        if img.height > 400 or img.width > 300:
            output_size = (400, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.avatar.path)
