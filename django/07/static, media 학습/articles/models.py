from django.db import models

# def 미디어파일상세경로함수(i):

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # 사용자가 업로드한 사진 경로 저장할 ... 새로운 필드 생성
    # blank=True : 빈 문자열로도 저장 가능!
    # 이미지 필드 사용하려면 라이브러리 설치가 필요, pip install Pillow, freeze 꼬옥
    # 모델에 변경 사항있으면 makemigrations -> migrate 꼬옥!  
    # upload_to = 미디어 루트(실제저장) 이후의 파일 추가 경로~~
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
