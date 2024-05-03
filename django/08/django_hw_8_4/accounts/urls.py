from django.urls import path
# views 다 import 하니까..
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    # 표시가 안 되어도 주소는 있어야지..
    path('logout/', views.logout, name='logout'),
]
