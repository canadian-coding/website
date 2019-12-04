from django.db import models
from datetime import datetime

from markdownx.models import MarkdownxField # From django-markdownx

# Create your models here.

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

class Author(models.Model):
    """Used to represent the author of posts & courses"""

    # Author information
    first_name = models.CharField(max_length = 75)
    last_name = models.CharField(max_length = 75)
    description = models.TextField()

    # Job information
    company = models.CharField(max_length = 75, blank=True)
    title = models.CharField(max_length = 75, blank=True)

    # Optional favourite/preferred language
    favourite_language = models.CharField(max_length = 100, blank=True, choices = language_choices)

    # Social media links
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
    """Drives the post_index and details view"""

    post_categories = [
        ("language-essentials", "Language Essentials"), # Builtin libraries and language constructs
        ("module-showcase", "Module Showcase"),         # Showing off a simple language add-on
        ("language-overview", "Language Overview"),     # Looking at language from a high-level overview
        ("project-showcase", "Project Showcase"),       # Showing off full-fledged apps
    ]
    # Primary post metadata
    title = models.CharField(max_length = 75)
    subheading = models.CharField(max_length = 125)
    author = models.ForeignKey(Author, default=1, on_delete=models.SET_DEFAULT)
    language = models.CharField(max_length = 100, choices = language_choices)
    category = models.CharField(max_length = 100, choices = post_categories, default = 1)

    # External links to social media
    github_source = models.URLField(default = "https://github.com/canadian-coding/posts/tree/master/")
    instagram_link = models.URLField(default = "https://www.instagram.com/canadiancoding/")

    # Primary post content
    content = MarkdownxField()

    # Creation and routing metadata
    created = models.DateField(blank = True)
    last_modified = models.DateTimeField(auto_now = True)
    post_slug = models.SlugField(blank = True, default=title)

    def __str__(self):
        """Sets display in admin view"""
        return self.title
    class Meta:
        """Used to overwrite model attributes"""
        verbose_name_plural = "Posts"


class DemoFiles(models.Model):
    """Used to showcase a demo in a post"""
    title = models.CharField(max_length = 50)
    contents = models.TextField()
    posts = models.ManyToManyField(Posts)

    def __str__(self):
        """Sets display in admin view"""
        return f"{self.title}"

    class Meta:
        """Used to overwrite model attributes"""
        verbose_name_plural = "Demo Files"
