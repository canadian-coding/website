from django.contrib import admin

# Importing posts models
from .models import Author, DemoFiles, Posts


# Registering models with django's admin interface
admin.site.register(Author)
admin.site.register(DemoFiles)
admin.site.register(Posts)