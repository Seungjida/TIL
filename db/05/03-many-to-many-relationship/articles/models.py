from django.db import models
from django.conf import settings
# django에서는 User 모델을 '직접' 참조하지 않는다.
# from accounts.models import User

# Create your models here.
class Article(models.Model):
    # 그냥 외래키는 단수형
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # n대m의 관계는 복수형
    # 지금 user 역참조 할 때, n:1과 n:m에서의 역참조 구현이 똑같아서 역참조 매니저 이름을 무조건 변경해야 함!
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')

    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
