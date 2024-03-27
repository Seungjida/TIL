from django.urls import path
from . import views

# 무슨 앱을 위한 url인지 명확하게 namespace 확정지어 놓자
app_name = 'articles'

urlpatterns = [
    # url -> view -> template(없을수도)
    # '경로/', 실행될 view 함수, pattern name
    path('', views.index, name='index'),
    path('create/', views.create, name='create')
]
