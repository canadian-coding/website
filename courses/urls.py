from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^$", views.index, name = "index"), # The posts homepage
    url(r"^module/(?P<id>\d+)/$", views.module_by_id, name = "module_by_id"),
    url(r"^course/(?P<code>\w+)-(?P<number>\d+)/module/(?P<module_number>\d+)/$", views.module_by_name, name = "module_by_name"),
    url(r"^course/(?P<code>\w+)-(?P<number>\d+)/$", views.course_overview_by_code, name = "course_overview_by_code"),
    url(r"^course/id/(?P<id>\d+)/$", views.course_overview_by_id, name = "course_overview_by_id"),
    ]