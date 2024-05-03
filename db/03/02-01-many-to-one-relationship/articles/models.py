from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # 외래키 필드(N쪽에), 참조하는 모델의 단수형
    # article 객체 덩어리 넣으면 알아서 들어감
    # article의 pk가 들어감
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
