from django.db import models
from datetime import datetime


from markdownx.models import MarkdownxField # From django-markdownx

typing_disciplines = [
    #(key, displayed_value)
    ("weakly-typed", "Weakly Typed"),
    ("strongly-typed", "Strongly Typed"),
    ("statically-typed", "statically Typed"),
    ("dynamically-typed", "Dynamically Typed"),
]

paradigms = [
    #(key, displayed_value)
    ("imperative", "Imperative"),
    ("concurrent", "Concurrent"),
    ("object-oriented", "Object oriented"),
    ("functional", "Functional"),
    ("procedural", "Procedural"),
]

syntax_concepts = [
    #(key, displayed_value)
    ("semicolons", "Semicolons"),
    ("indentation", "Indentation"),
    ("curly-braces", "Curly Braces"),
    ("slash-comments", "Slash Comments"),
    ("hash-comments", "Hash Comments"),
]

class Language(models.Model):
    """Represents programming languages"""
    name = models.CharField(max_length = 75)
    website = models.URLField(blank=True)
    language_creation = models.DateField()
    used_by = models.CharField(max_length = 200)

    resources = MarkdownxField()
    commenting = MarkdownxField()
    variables = MarkdownxField()
    functions = MarkdownxField()
    running = MarkdownxField()

    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        """Sets display in admin view"""
        return self.name

    class Meta:
        """Used to overwrite model attributes"""
        verbose_name_plural = "Languages"

class Paradigms(models.Model):
    """Represents programming paradigms"""
    name = models.CharField(max_length = 75)
    description = MarkdownxField()
    languages = models.ManyToManyField(Language, blank = True)

    def __str__(self):
        """Sets display in admin view"""
        return self.name
        
    class Meta:
        """Used to overwrite model attributes"""
        verbose_name_plural = "Paradigms"

class Typing(models.Model):
    """Represents programming typing disciplines"""
    name = models.CharField(max_length = 75)
    description = MarkdownxField()
    languages = models.ManyToManyField(Language, blank = True)

    def __str__(self):
        """Sets display in admin view"""
        return self.name
        
    class Meta:
        """Used to overwrite model attributes"""
        verbose_name_plural = "Typing Disciplines"

class Syntax(models.Model):
    """Represents programming language syntax details"""
    name = models.CharField(max_length = 75)
    description = MarkdownxField()
    languages = models.ManyToManyField(Language, blank = True)

    def __str__(self):
        """Sets display in admin view"""
        return self.name
        
    class Meta:
        """Used to overwrite model attributes"""
        verbose_name_plural = "Syntax Details"