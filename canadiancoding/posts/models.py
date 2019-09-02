from django.db import models
from datetime import datetime

#from multiselectfield import MultiSelectField # From django-multiselectfield
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

    post_categories = [
        ("language-essentials", "Language Essentials"), # Builtin libraries and language constructs
        ("module-showcase", "Module Showcase"), # Python
        ("package-showcase", "Package Showcase"), # Go
        ("language-overview", "Language Overview"),
        ("project-showcase", "Project Showcase"), # Showing off full-fledged apps
    ]
    title = models.CharField(max_length = 75)
    subheading = models.CharField(max_length = 125)
    language = models.CharField(max_length = 100, choices = language_choices)
    category = models.CharField(max_length = 100, choices = post_categories)
    github_source = models.URLField(default = "https://github.com/canadian-coding/posts/tree/master/")
    instagram_link = models.URLField(default = "https://www.instagram.com/canadiancoding/")
    content = MarkdownxField()
    created = models.DateField(blank = True)
    last_modified = models.DateTimeField(auto_now = True)
    def __str__(self):
        """Sets display in admin view"""
        return self.title
    class Meta:
        """Used to overwrite model attributes"""
        verbose_name_plural = "Posts"