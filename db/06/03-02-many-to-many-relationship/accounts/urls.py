from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    # 유저네임도 variable routing으로 쓸 수 있음! 안 겹치게 하기 위해서도 필요할 수 있엉
    # variable routing 할 때는 앞에 키워드를 붙이는 게 좋아
    # 그렇게 하지 않고 맨 앞에 path가 갈 경우, 동일한 타입의 variable 오기만 하면 글로만 감
    path('profile/<str:username>/', views.profile, name='profile'),
    # 상대방 조회
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
