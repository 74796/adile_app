from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime


class TodoTask(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)
    deadline_time = models.DateTimeField()

    def is_expired(self):
        return self.deadline_time < datetime.datetime.now()
