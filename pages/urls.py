from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^$", views.index, name = "index"), # The site homepage
    url(r"services", views.service, name = "services"), # The site homepage
    url(r"terms-of-service", views.terms_of_service, name = "terms_of_service"), # The site homepage
    url(r"google4872331c416f8761.html", views.google_verification, name = "google_verification"), # Required for youtube verification
]