from django.conf.urls import url
from . import views


urlpatterns = [
    url(r"^$", views.index, name = "index"), # The posts homepage
    url(r"^post/(?P<id>\d+)/$", views.details, name = "details"), # Details page; accessed based on post ID
    url(r"^post/(?P<language>\w+)/(?P<slug>.*)/$", views.details_by_slug, name = "details_by_slug"), # Details page; accessed based on post language, and slug
]