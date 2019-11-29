from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts, language_choices, DemoFiles

# Used to calculate how many months of posts have happened
from datetime import datetime
from dateutil import relativedelta
# Create your views here.

def index(request):

    posts = Posts.objects.order_by('-created')
    first_post = datetime(2019, 6, 23)

    difference = relativedelta.relativedelta(datetime.now(), first_post)
    languages = len(language_choices)
    context = {
        'title': "Home",
        'posts': posts,
        'difference': difference,
        'languages' : languages
    }

    return render(request, "posts_index.html", context)


def details(request, id):
    post = Posts.objects.get(id=id)
    files = DemoFiles.objects.filter(posts=id)
    context = {
        'files':files,
        'post': post,
    }
    return render(request, "posts/details.html", context)
    