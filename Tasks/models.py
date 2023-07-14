from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid


class Task(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag = models.CharField(max_length=120)
    text = models.TextField()
    to_date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        db_table = 'tasks'
        ordering = ['to_date']
        
