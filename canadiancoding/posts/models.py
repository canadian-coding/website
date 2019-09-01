from django.db import models
from datetime import datetime

from multiselectfield import MultiSelectField # From django-multiselectfield
from markdownx.models import MarkdownxField # From django-markdownx

# Create your models here.

class Posts(models.Model):
    language_choices = [
       #(key, displayed_value)
        ("python", "Python"),
        ("go", "Go"),
        ("c", "C"),
        ("rust", "Rust"),
        ("javascript", "JS"),
        ("html", "HTML"),
        ("processing", "Processing"),
    ]
    title = models.CharField(max_length=150)
    subheading = models.CharField(max_length=150)
    languages = MultiSelectField(choices=language_choices)
    github_source = models.URLField()
    content = MarkdownxField()
    created = models.DateField(blank=True)
    last_modified = models.DateTimeField(auto_now = True)
    def __str__(self):
        """Sets display in admin view"""
        return self.title
    class Meta:
        """Used to overwrite model attributes"""
        verbose_name_plural = "Posts"