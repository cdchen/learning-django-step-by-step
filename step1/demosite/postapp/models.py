from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    create_time = models.DateTimeField(db_index=True, auto_now_add=True)
