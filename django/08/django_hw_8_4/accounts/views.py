from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
# 유저 정보 저장하는 모델이니까~ 대신 이미 abstract이 있어서 좀 간편하게 만든 모델

# 리다이렉트 해도 리퀘스트가 있고 그 안에 쿠키(세션 id도 당연히)가 있데이
# 그래서 얘가 지금 로그인 한 건지 안 한 건지 앎
def index(request):
    all_users = User.objects.all()
    context = {
        'all_users' : all_users,
    }
    return render(request, 'accounts/index.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:    
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

