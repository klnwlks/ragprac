from django.db import models

# Create your models here.
from django.contrib.postgres.fields import ArrayField

class Conversation(models.Model):
    title = models.CharField()
    made = models.DateField()
    messages = models.JSONField(default=list, blank=True)
    f_documents = models.JSONField(default=list, blank=True)