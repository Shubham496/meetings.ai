# meetingsAI/dashboard/models.py
from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()

    def __str__(self):
        return self.title
