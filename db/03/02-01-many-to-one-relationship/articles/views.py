from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # 게시글 조회
    article = Article.objects.get(pk=pk)
    # 특정 게시글에 작성된 모든 댓글 조회 (Article -> Comment, 역참조)
    # 역참조대상_set은 objects같은 매니저임~
    comments = article.comment_set.all()
    # Comment.objects.all() : DB의 모든 댓글을 조회(특정 게시글에 작성된 모든 댓글 조회가 아님)

    # 사용자로부터 댓글 데이터 입력을 받기 위한 form
    # detail은 지금 form으로 뭘 보내고 이런 게 아님..
    # 폼 자체를 보여주긴 해야하니까 보내는 거임
    comment_form = CommentForm()
    context = {
        'article': article,
        # 지금 db에 있는 현재 article에 저장된 comments
        'comments' : comments,
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)

def comments_create(request, pk):
    # 게시글 조회(댓글은 게시글이랑 관련이 있기 때문에 먼저 어떤 게시글에 작성되어야 하는지 알아야 한다)
    article = Article.objects.get(pk=pk)
    # 게시글에 작성된 comment들을 받아 옴
    comments = article.comment_set.all()
    # 사용자 입력 데이터를 받아서 Comment 저장(+ 유효성 검사)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        # 저장이 이루어지기 전에 comment 인스턴스를 제공받는 게 필요
        # save 메서드의 commit 속성, DB에 저장하지 않고 인스턴스만 반환
        comment = comment_form.save(commit=False)
        # 외래키 채움
        comment.article = article
        # 진짜로 저장
        comment.save()
        return redirect('articles:detail', article.pk)
    # 무조건 post로 받기 때문에 else고 뭐고 할 게 없음

    # 현재! 댓글폼에 작성된 게 없다면~ 그냥 지금 가지고 있는 context로 detail.html 랜더링하는데,,
    # form 자체를 화면에 보여주긴 해야하니까 같이 context로 보냄
    context = {
        'comment_form' : comment_form,
        'article' : article,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)

def comments_delete(request, article_pk, comment_pk):
    # 어떤 댓글을 삭제하는지 조회
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    # 디테일에서는 article 가지고 이것저것하니께
    return redirect('articles:detail', article_pk)