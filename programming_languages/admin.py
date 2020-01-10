from django.contrib import admin

# Register your models here.
from .models import Language, Paradigms, Typing, Syntax

admin.site.register(Language)
admin.site.register(Paradigms)
admin.site.register(Typing)
admin.site.register(Syntax)