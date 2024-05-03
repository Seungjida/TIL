from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 직접 참조하면 이름바꾸거나 할 때 힘들어
        # 현재 활성화된 유저 객체 알아서 리턴
        model = get_user_model()

# admin이랑 사용하는 form이 똑같아서 수정이 필요
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        # 현재 활성화된 유저 객체 알아서 리턴
        model = get_user_model()
        # django user object -> auth 공식문서에 있는 fields 봐라
        # 비밀번호 바꾸는 form을 당장 가리기는 어려울 듯.. 나중에
        fields = ('first_name', 'last_name', 'email',)
        # exclude