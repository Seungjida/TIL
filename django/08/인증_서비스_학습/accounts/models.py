from django.db import models
# 기존 유저 모델 클래스
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 추상 클래스는 설계도나 테이블 안 만들어 짐, 그냥 도움만 줌..^^
class User(AbstractUser):
    pass    # 일단 뭐 안 바꿈 그대로 적용 근데 이렇게 클래스를 만들어주는게 좋아