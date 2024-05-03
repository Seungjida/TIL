from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
# admin site에도 지금 등록한 User모델이 잘 나오도록 등록
# 원래는 기본 값으로 출력이 잘 설정되어 있지만 바꾸고는 그렇지 않기 때문에 등록해주어 함
admin.site.register(User, UserAdmin)