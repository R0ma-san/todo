from django.db import models

class Task(models.Model):
    body = models.TextField()
    estimated_finish_time = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    
