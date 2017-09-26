from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render

User = get_user_model()

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


def post_add(request):
    # 강사님 git 코멘트 확인
    if request.method == 'POST':
        post = Post(
            title=request.POST['title'],
            content=request.POST['content'],
            author=User.objects.get(username='darkblank')
        )
        post.publish()
        return HttpResponse(f'{post.title}, {post.content}')
    elif request.method == 'GET':
        context = {

        }
        return render(request, 'blog/post_form.html', context)
