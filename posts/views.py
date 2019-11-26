from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

# Create your views here.

def index(request):

    posts = Posts.objects.order_by('created')

    context = {
        'title': "Home",
        'posts': posts,
    }

    return render(request, "posts_index.html", context)


def details(request, id):
    post = Posts.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, "posts/details.html", context)
    