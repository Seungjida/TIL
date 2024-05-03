from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # 한 게시물에 대해 자세하게 보여주는 부분 ~^
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    # 게시글 조회용, article_id에 들어갈 pk를 받아와야함
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    # 댓글 삭제
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_dedete'),
]
