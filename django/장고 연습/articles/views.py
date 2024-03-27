from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.
def index(request):
    # return render(request, C:\Users\SSAFY\Desktop\오늘\장고 연습\articles\templates...,)
    articles = Article.objects.order_by('-pk') # pk기준 내림차순 정렬
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html',context)

def create(request):
    '''
        1. 생성하기 위한 데이터를 입력할 수 있는 페이지
        2. 생성한 데이터를 토대로 실제로 데이터를 생성하는 함수
    '''
    # 사용자 방식에 따라 조건 분기
    if request.method == 'POST':    # POST 요청이 올려면 GET 요청 처리가 먼저이다.
        form = ArticleForm(request.POST)    # 사용자가 post 보낸 거에 데이터가 있음, 사용자가 넣은 내용 담아서 다시 form 만듦
        if form.is_valid(): # 상속 받은 modelform에 정의되어 있던 유효성 검사 메서드
            # 유효성 검사 메서드 통과 : db에 저장할 수 있을 거 같음
            # form field를 내가 지정하니까 항상 모든 필드에 대한 정보를 받는 게 아니므로,
            # 사용자가 보내온 데이터가 정의된! field에 삽입하기 적절하다~

            form.save() # model = Article 넘겨줬으니 거기서 난 save.. 저장했움!

            return redirect('articles:index')
    else:
        # GET 요청이 들어왔을 때는 article 생성 할 수 있는 form 랜더링
        form = ArticleForm()
    context = {
        'form': form
    }
    # form들 template에 같이 넘겨줌
    return render(request, 'articles/create.html', context)