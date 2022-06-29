from django.shortcuts import render
from .models import Blogs
# Create your views here.


def view_blog(request):
    """ View to render blog posts """

    posts = Blogs.objects.all()

    template = 'blog/blog.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)