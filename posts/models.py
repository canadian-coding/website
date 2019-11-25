from django.db import models
from datetime import datetime

#from multiselectfield import MultiSelectField # From django-multiselectfield
from markdownx.models import MarkdownxField # From django-markdownx

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length = 75)
    last_name = models.CharField(max_length = 75)
    description = models.TextField()
    company = models.CharField(max_length = 75, blank=True)
    title = models.CharField(max_length = 75, blank=True)
    languages = models.CharField(max_length = 100, blank=True)
    github_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)

    def __str__(self):
        """Sets display in admin view"""
        return f"{self.first_name}  {self.last_name}"

    class Meta:
        """Used to overwrite model attributes"""
        verbose_name_plural = "Authors"

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
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
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
