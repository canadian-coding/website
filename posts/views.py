from django.shortcuts import render
from django.http import HttpResponse

# Importing posts app models
from .models import Posts, language_choices, DemoFiles

# Used to calculate how many months of posts have happened
from datetime import datetime
from dateutil import relativedelta

def index(request):
    """Renders the /posts route as post_index.html
    Route: /posts
    """

    posts = Posts.objects.order_by('-created') # Collects posts in reverse chronological order LIFO

    # Values passed to the counter on the post homepage

    # Used to calculate time delta from first post to current month
    first_post = datetime(2019, 6, 23) 
    difference = relativedelta.relativedelta(datetime.now(), first_post)

    # Counting how many programming languages posts have been made for
    languages = len(language_choices)

    # Passing variables as context map to the template
    context = {
        'title': "Home",
        'posts': posts,
        'difference': difference,
        'languages' : languages
    }

    return render(request, "posts_index.html", context)


def details(request, id):
    """Used to render posts based on post ID
    Route: /posts/post/(?P<id>\d+)/
    """
    post = Posts.objects.get(id=id) # Select post based on provided id

    files = DemoFiles.objects.filter(posts=id) # Get associated files based on post id

    # Passing variables as context map to the template
    context = {
        'files':files,
        'post': post,
    }
    return render(request, "posts/details.html", context)

def details_by_slug(request, language, slug):
    """Used to render post based on language, and post slug
    Route: /posts/post/(?P<language>\w+)/(?P<slug>\w+)
    """
    # Gather post based on language and slug
    post = Posts.objects.filter(language=language).get(post_slug = slug)

    files = DemoFiles.objects.filter(posts=post.id) # Get associated files based on post id

    # Passing variables as context map to the template
    context = {
        'files':files,
        'post': post,
    }
    return render(request, "posts/details.html", context)
    