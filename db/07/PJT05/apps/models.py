from django.db import models

# Create your models here.
# 키워드 & 게시글 제목

class Article(models.Model):
    title = models.TextField()
    # 원래는 게시글이 다른 키워드로도 나와야하니까 M:N구조임..ㅋㅋ
    Query = models.ForeignKey(Query, on_delete=models.DO_NOTHING)

class Query(models.Model):
    keyword = models.TextField()
