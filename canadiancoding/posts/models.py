from django.db import models
from datetime import datetime

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    created = models.DateTimeField(default = datetime.now, blank=True)
    def __str__(self):
        """Sets display in admin view"""
        return self.title
    class Meta:
        """Used to overwrite model attributes"""
        verbose_name_plural = "Posts"