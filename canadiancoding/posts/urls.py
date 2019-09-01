from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^$", views.index, name = "index"), # The posts homepage
    url(r"^details/(?P<id>\d+)/$", views.details, name = "details"),
]