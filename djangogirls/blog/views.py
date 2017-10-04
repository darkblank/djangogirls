from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import Post

User = get_user_model()


def post_list(request):
    posts_filter = Post.objects.filter(published_date__isnull=False)
    paginator = Paginator(posts_filter, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
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
    # 아래의 get은 dictionary 메서드
    if request.method == 'POST':
        # request.POST(dict형 객체)에서 'title', 'content'키에 해당하는 value를 받아
        # 새 Post객체를 생성 (save() 호출없음. 단순 인스턴스 생성)
        # 생성한 후에는 해당 객체의 title, content를 HttpResponse로 전달

        # title이나 content값이 오지 않았을 경우에는 객체를 생성하지 않고 다시 작성페이지로 이동 (render또는 redirect)
        #   extra) 작성페이지로 이동 시 '값을 입력해주세요'라는 텍스트를 어딘가에 표시 (render)
        #   extra*****) Bootstrap을 사용해서 modal띄우기
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_publish = bool(request.POST.get('is_publish'))
        author = User.objects.get(username='darkblank')

        # title과 content가 모두 전달되었을때만 Post생성
        if title and content:
            post = Post.objects.create(
                author=author,
                title=title,
                content=content,
            )
            if is_publish:
                post.publish()
            else:
                post.save()
            return redirect('post_detail', pk=post.pk)

        context = {
            'title': title,
            'content': content,
        }
    else:
        context = {}

    return render(request, 'blog/post_form.html', context)


def post_delete(request, pk):
    """
    pk에 해당하는 Post객체를 DB에서 삭제 (QuerySet.delete() 또는 Model.delete() 메서드 사용)
    :param request:
    :param pk: Post의 pk
    :return: redirect('post_list')
    """
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()

        return redirect('post_list')
    return HttpResponse('Permission denied', status=403)
