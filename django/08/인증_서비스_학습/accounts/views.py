from django.shortcuts import render, redirect
# 직접 form을 안 만들어도 됨, 인증쪽은 개발자가 직접 작성하기 어려워
from django.contrib.auth.forms import AuthenticationForm
# login 함수 import, 장고가 알아서 세션데이터 생성하고 id 발급해줌, 이름 충돌 방지하기 위해 별명 붙임
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.
# 세션 데이터 생성
def login(request):
    # 로그인 로직 진행
    if request.method == 'POST':
        # id, pw 데이터로 form을 만듦
        # modleform 아니고 그냥 form이라 내가 만든 db에 원래는 저장이 안 되니까 데이터를 인자로 받을 필요 없다고 생각할 수 있지만,
        # 받은 값을 로그인 로직에 활용해야하니까 인자로 줌
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # form.save() 계정 만드냐
            # form은 사용자 입력 정보가 담긴 form! 유효성 검사 완료된 정보만 뽑아
            auth_login(request, form.get_user())
            return redirect('articles:index')
    # 입력값 받음
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
        # context processors, 이미 context에 들어가 있음, 모든 템플릿에서 user에 접근 가능 : django.contrib.auth.context_processors.auth
        # user라는 이름 올려서 출력하면 안 됨
    }
    return render(request, 'accounts/login.html', context)

# 서버에 있는 데이터와 브라우저에 있는 id(개발자도구 - 쿠키 - 어플리케이션에 보면 나옴), 양쪽 다 지워줌
def logout(request):
    auth_logout(request)
    return redirect('articles:index')