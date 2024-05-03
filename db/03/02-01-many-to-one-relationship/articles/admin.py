from django.contrib import admin
from .models import Article, Comment

# Register your models here.
admin.site.register(Article)
# admin 페이지에서 보여지게 하려면
admin.site.register(Comment)