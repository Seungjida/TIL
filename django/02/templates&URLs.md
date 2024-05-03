1.  템플릿 상속
템플릿 : 표현 제어 및 관련된 부분 담당

Django Template Langage(DTL): 조건, 반복, 변수 등의 프로그래밍적 기능을 제공
- {{variable}} 딕셔너리 값을 해당 view 함수의 세번째 인자로 넘겨줌
- {{variable | filter}} 연결이 가능하며 일부 필터는 인자를 받기도 함
- {% tag %} 반복 또는 논리를 수행하여 제어 흐름을 만듦, 시작과 종료 태그가 필요한 경우도 있다, 주석도 이걸로 가능
ex) {% for %} {% endfor%}

같은 구조를 쓰는 템플릿의 코드를 계속 다시 작성해야할 필요가 있을까 ??
템플릿 상속: 페이지의 공통요소를 포함하고 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 스켈레톤 템플릿을 작성하여 상속 구조를 구축
- 상속 구조 만들기: {% block 이름 %} {% endblock 이름 %}
- 하위 템플릿: {% extends '경로.html' %}(최상단에 작성)  
{% block 이름 %} 재정의 할 부분 {% endblock 이름 %}
저 사이 부분말고 나머지는 그대로 상속

=> 명칭만 그런 거지 python 코드로 실행되는 것이 아님, 프로그래밍적 로직은 view 함수에 작성

2.  HTML form

HTML 'form' element(http 요청을 서버에 보냄)를 통해 사용자와 애플리케이션 간의 상호작용 이해하기

!!!!!!!! 요청
- <form action='보낼 서버 url/' method='GET'> : 사용자로부터 할당된 데이터를 서버로 전송
  text, password, checkbox 등 여러 방식 제공
  action 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐

- label: 폼 요소에 라벨 붙여주는 거
 명시적 작성 방법: <label for = 'input 태그의 id값'></label><input type='text' id='name'>
 label 태그와 input 태그를 따로 사용하며 for 속성을 통해 연결
 암시적 작성 방법: <label><input type='number'> </label>
 label 태그 안에 input 태그를 넣어 속성 없이 암시적으로 연결

- input: 사용자의 데이터를 입력 받을 수 있는 요소
  name 속성: 입력한 데이터에 붙이는 이름
  input의 name 속성 = input의 입력한 데이터, key=value

!!!!!!!! 응답
HTTP request 객체: form으로 전송한 데이터 뿐만 아니라 모든 요청 관련 데이터가 담겨 있음(view 함수의 첫번째 인자)
form 데이터 가져오는 방법: request.GET.get('input의 name 속성'), 딕셔너리 값에 넣어 reder 호출하면서 인자로 넘겨줌(리스트지만 접근하면 자동으로 풀림)

+ 템플릿 기본 경로(app 안에 templates 안) 외 커스텀 경로 추가하기
# settings.py
BASE_DIR: settings에서 경로 지정을 편하게 하기 위해 최상단 지점을 지정 해놓은 변수 (걍 파일 그자체), settings.py의 부모의 부모~~
'DIRS' : [BASE_DIR / '새롭게 만든 폴더', ]


3.  Django URLs
URL dispatcher: URL 패턴을 정의하고, 해당 패턴이 일치하는 요청을 처리할 view 함수를 매핑

Variable Routing: URL 일부에 변수(view 함수의 인자로 전달 가능)를 포함시키는 것
ex) path('articles/<int:num>/', views.detail) : <path_converter:variable_name>
view 함수에서 매개변수 하나 더 받아야 함~~~~ (여기선 num)