from django.urls import path
from . import views

# 더이상 name 필요 없다 ! 템플릿에서 주소 안 쓸 거고 사용자에게 직접적으로 제공할 필요 없지
urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
]
