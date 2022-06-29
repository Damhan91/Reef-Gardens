from django.shortcuts import render
from .models import Blog


def view_blog(request):
    """ View to render blog posts """

    posts = Blog.objects.all()

    template = 'blog/templates/blog.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)
