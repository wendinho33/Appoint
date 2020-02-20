from django.db import models
from django.utils import timezone


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
