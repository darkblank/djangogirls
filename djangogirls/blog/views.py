from django.http import HttpResponse
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


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse('페이지가 없습니다')

    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)
