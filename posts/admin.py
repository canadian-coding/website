from django.contrib import admin

# Register your models here.

from .models import Author, DemoFiles, Posts



admin.site.register(Author)
admin.site.register(DemoFiles)
admin.site.register(Posts)