from django import forms
from .models import Article

'''
    둘 다 class에 상속 시켜줄 class !!
    Form -> 모델에 대한 정보가 없는 form을 위한 클래스
    ModelForm -> 모델에 대한 정보가 있는 Form을 위한 클래스
'''

# # 인증 관련된 부분은 그냥 form 쓰는 경우가 많다..
# class ArticleForm(forms.Form):
#     # 모델에 대한 정보 없이 form 구성하려면, 적절한 field를 내가 직접 구성
#     # 장고 모델 정의하는 거랑 똑같다

#     title = forms.CharField(max_length=100)
#     content = forms.CharField()
#     is_hidden = forms.BooleanField()
#     # ... 모델에 있는 거 내가 다시 또 써야함? 정보가 있ㄴ느데...

class ArticleForm(forms.ModelForm):
    # 필드명을 변수로
    title = forms.CharField(
        max_length=100,
        # form 내부에서 보여줄 input을 어떻게 정의할 것인가.
        # 어떤 input으로 누가 만들어 주는데?
        # html 태그는 여러 개의 속성을 가지고 있는 데 이를 쓰는 방법은 '속성명="값" == 키:값'
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder' : '제목을 입력하세요'
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder' : '내용을 입력하세요'
            }
        )
    )

    # html에서 사용할 form 태그를 구성할 필드 정보를 원하는 모델로부터 받아온다.
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title', 'content', 'is_hidden',) 필드 정보 적을 때는 튜플 써야함, 불변!
        
        # 내가 가진 필드 중에 어떤 필드의 속성만 간단하게 수정하고 싶다.
        widgets = {
            'is_hidden':forms.RadioSelect(
                attrs={
                    'class': 'form-check'
                },
                choices=(
                    (True, '비공개'), (False, '공개')
                )
            )
        }