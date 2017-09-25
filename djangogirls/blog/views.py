from django.shortcuts import render

# Create your views here.
from blog.models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False)
    context = {
        # posts key의 value는 QuerySet
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)
