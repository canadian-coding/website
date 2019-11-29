from django.db import models

# Create your models here.
from markdownx.models import MarkdownxField # From django-markdownx
from posts.models import Author, language_choices


class Course(models.Model):
    code = models.CharField(max_length = 9)
    short_description = models.CharField(max_length = 75)
    full_description = MarkdownxField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    language = models.CharField(max_length = 100, choices = language_choices)
    github_link = models.URLField(blank=True)
    youtube_playlist_link = models.URLField(blank=True)

    def __str__(self):
        """Sets display in admin view"""
        return f"{self.code}: {self.short_description}"

    class Meta:
        """Used to overwrite model attributes"""
        verbose_name_plural = "Courses"

class Module(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length = 75)
    author = models.ForeignKey(Author, default=1, on_delete=models.SET_DEFAULT)
    course = models.ForeignKey(Course, default=1, on_delete=models.SET_DEFAULT)
    next_module = models.ForeignKey('self', default=1, on_delete=models.SET_DEFAULT, blank=True, related_name = "next", null=True)
    previous_module = models.ForeignKey('self', default=1, on_delete=models.SET_DEFAULT, blank=True, related_name = "previous",null=True)
    language = models.CharField(max_length = 100, choices = language_choices)
    github_link = models.URLField(blank=True)
    youtube_id = models.CharField(max_length=11, blank=True)
    content = MarkdownxField()
    exercises = models.TextField()
    challenges = models.TextField()
    solutions = models.TextField()



    def __str__(self):
        """Sets display in admin view"""
        return f"{self.number}: {self.title}"

    class Meta:
        """Used to overwrite model attributes"""
        verbose_name_plural = "Modules"