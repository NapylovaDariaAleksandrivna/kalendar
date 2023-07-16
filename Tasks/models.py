from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid
from PIL import Image

from django.core.files.uploadedfile import SimpleUploadedFile
class Task(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4)
    tag = models.CharField(max_length=120)
    text = models.TextField(blank=True)
    to_date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(
        upload_to='image',
        blank=True,
    )
    def __str__(self):
        return f'Профиль {self.tag} '
    
    