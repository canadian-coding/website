from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^$", views.index, name = "index"), # The site homepage
    url(r"services", views.service, name = "services"), # The site homepage
]