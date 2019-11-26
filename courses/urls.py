from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^$", views.index, name = "index"), # The posts homepage
    url(r"^module/(?P<id>\d+)/$", views.module, name = "module"),
    url(r"^course/(?P<id>\d+)/$", views.course_overview, name = "course_overview"),
]