from django.urls import path
from . import views

app_name = 'libraries'
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:author_pk>/', views.detail, name='detail'),
]
