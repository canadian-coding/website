from django.db import models

from datetime import datetime

from programming_languages.models import Language
from posts.models import Author

from markdownx.models import MarkdownxField # From django-markdownx

class Project(models.Model):
    """Generic software project class"""

    # Primary post metadata
    title = models.CharField(max_length = 75)

    author = models.ForeignKey(Author, default = 1, on_delete = models.SET_DEFAULT)
    languages = models.ManyToManyField(Language, blank = True)

    # Creation and routing metadata
    created = models.DateField(blank = True)
    last_modified = models.DateTimeField(auto_now = True)
    post_slug = models.SlugField(blank = True, default = title)

    # External links to social media
    source_code = models.URLField(blank = True)
    website = models.URLField(blank = True)
    package_provider = models.URLField(help_text = "pypi.org, crates.io etc.", blank = True) # i.e. pypi.org, crates.io etc.

    # Primary post content
    description = MarkdownxField()

    def __str__(self):
        """Sets display in admin view"""
        return self.title

    class Meta:
        """Used to overwrite model attributes"""
        verbose_name_plural = "Projects"