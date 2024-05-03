from django.db import models
# 장고에서는 user모델을 '직접' 참조하지 않는다.
# from accounts.models import User
from django.conf import settings    # 문자열을 반환, User 객체가 models.py보다 더 늦게 구동되는 듯.. 그래서 일단 문자열을 집어 넣고..참조하는데에 있어서 큰 문제는 없다잉

# Create your models here.
class Article(models.Model):
    # 테이블은 기본적으로 not null, null 값을 넣어서는 안된다!!@ @! 이미 db에 데이터가 생성되어 있으면 기본값을 만들어 넣어줘야 함
    # 모델 클래스를 초기에 작성할 때는 단순히 필요한 필드를 정의하고, 새로운 필드를 추가할 때는 이미 존재하는 데이터베이스와의 호환성을 고려하여 변경 사항을 신중하게 처리해야 합니다.
    # 초기 작성과 새로운 필드 추가는 좀 다른 개념~~
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # 댓글이랑 유저도 관계를 맺어보자!~!@!@
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
