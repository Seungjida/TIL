from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

'''
Article(N) -> User(1) (참조) : article.user
User(1) -> Article(N) (역참조, 역참조 매니저 이용) : user.article_set.all() 
'''
@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # 외래키가 생겼으니까 바로 테이블에 레코드 쓰면 안 됨
            article = form.save(commit=False)
            # 그럼 게시글 작성 요청 유저가 누구?
            # 지금 로그인해서 리퀘스트 보내는 유저!
            # get_model_user()는 안 되나? 되는데.. 저게 더 간편하고 직관적인 방법! 
            article.user = request.user
            article.save()
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
    # 수정요청자와 작성자 비교
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 수정요청자와 작성자 비교
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                # commit=False 안 해도 애초에 form 만들 때 artile 넣어줌
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    # 일치 안 하면 수정 안 하고 메인페이지로 리다이렉트
    else:
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)

'''
Comment(N) -> User(1) (참조) : comment.user
User(1) -> Comment(N) (역참조, 역참조 매니저 이용) : user.comment_set.all() 
'''

# 로그인한 사용자는 통과하고 비로그인 사용자는 로그인 페이지로 리다이랙트 시킴
# 원래 post로만 보내니까 굳이 확인 안 했지만 정석이라면 해야 함
# 데코레이터는 순서 고려
@login_required
@ require_POST
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.all()
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        # 댓글 작성자가 누군데?
        # article 작성자랑 달라도 되겠지?
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'comment_form': comment_form,
        'article': article,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    # 댓글 삭제 요청자가 댓글 작성자 본인이냐?
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)
