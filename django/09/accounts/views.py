from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
def login(request):
    # 로그인 상태면 주소를 이용해 강제로도 못 감
    # request에 session 있지용

    # 인증된 사용자냐?(이미 로그인 되어 있음?)
    # 속성값이라서 ()로 호출 ㄴㄴ
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        # AuthenticationForm은 받은 사용자명과 비밀번호를 데이터베이스에 있는 계정 정보와 비교하여 사용자를 인증
        # 내부적으로 authenticate() 함수를 사용하여 사용자를 인증. 이 함수는 받은 사용자명과 비밀번호를 사용하여 데이터베이스에서 해당 사용자를 찾고, 인증에 성공하면 해당 사용자 객체를 반환. 
        form = AuthenticationForm(request, request.POST)
        # form이 형식에 맞는지만 검사
        if form.is_valid():
            # 로그인 상태로 만듦, 어? 상태? 세션!
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    # 로그인 상태면 주소를 이용해 강제로도 못 감
    # 그냥 user.is_authenticated는 template에서 컨텍스트에 자동으로 user을 받았을 때 가능한 거지 지금은 아니잔하.. 여기는 뷰예욤~ 알됨안됨!
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        # model form이니까 인자구성(순서)이 이렇다
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            '''
            1. auth_login()의 두번째 인자로 그냥 request.user가 들어오면 안 되는 이유 ... ?

            -> request한 사용자와 지금 회원가입한 사용자가 같지 않을 수 있따.. 저장하며 반환받은 새로운 user로 로그인 해야 해요

            2. 두번째 인자로 그냥 user(컨텍스트 프로세서 관련)하면 안 되냐?
            
            -> 여기가 템플릿이냐. 인자로 안 넘겨줬다아이가, request만 넘겨줌

            '''
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

# 인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터..
# 비인증 사용자의 경우 '/accounts/login/'주소로 redirect 시킴! url이 중요하지욤?
@login_required
def delete(request):
    # request.User 자체가 유저 정보라서 유저 조회할 필요 없다
    request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)

# 세션은 사용자의 로그인 상태를 유지하고, 인증 정보를 관리하는 데 사용
# 현재 로그인 되어 있는 사용자가 비번을 바꾸면 새로운 세션 id가 부여됨(인증 정보 관련)
# 이전에 사용하던 세션은 더이상 안전하지 않을 수 있다 -> 이전에 접속한 기기에서 로그인 된 세션은 새로운 비밀번호로 인증되지 않아서 보안 상 문제가 있따!
@login_required
def change_password(request, user_pk):
    if request.method == 'POST':
        # 인자 : 유저, 데이터
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # 저장후에는 변경된 유저 객체 반환
            user = form.save()
            # 세션 변경 무효화, 사이트에 따라 달라
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        # model form하기에는 수정한 비밀번호가 그대로 db에 저장되는 것이 아니므로 form임
        # 인증과정을 거쳐 new 세션 데이터와 함께 저장
        # passwordChangeForm은 첫번째 인자 user가 필수(form인데 내부적으로 약간 수정된듯)
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)