from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post


def index(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'index.html', {'posts': posts})


def about(request):
    return render(request, 'about.html')


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin",
    ]

    return HttpResponse("\n".join(text), content_type="text.plain")
