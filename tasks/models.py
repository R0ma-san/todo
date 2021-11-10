from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    body = models.TextField()
    estimated_finish_time = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'tasks', null=True)
