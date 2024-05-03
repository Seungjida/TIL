from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        # filter()결과 반환 ㅇ근데 목록이 없으면 404 반환
        articles = get_list_or_404(Article)
        
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(
            article, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def comment_list(request):
    # 전체 댓글 조회
    comments = Comment.objects.all()
    # 직렬화
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # 단일 댓글 조회
    # get은 없으면 바로 예외 발생시킴! 더이상 그 밑으로 안 간데이
    # 그래서 없으면 무조건 500 에러 발생(정확한 에러가 아이데이)
    comment = Comment.objects.get(pk=comment_pk)

    # get_object_or_404는 get역할 하지만 객체가 없을 때 http404를 raise, 아니라면 try except 해얗 함

    if request.method == 'GET':
        # 직렬화
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # 수정
    elif request.method == 'PUT':
        # 이미 comment에 외래키가 있어서 안 넣어줘도 됨
        # 여기는 instance 그런 거 안 해도 되니ㅏ?
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def comment_create(request, article_pk):
    # 게시글 조회
    article = Article.objects.get(pk=article_pk)
    # 사용자 입력 데이터를 받아 직렬화 진행
    serializer = CommentSerializer(data=request.data)
    # 유효성 검사, 외래키 필드는 잠시 보류!!! 사용자가 직접 안 줄거니까~
    # 읽기 전용 필드: 유효성 검사에서는 제외, 데이터 조회 시에는 출력
    if serializer.is_valid(raise_exception=True):
        # 기존 모델 폼에서 쓰던 문법과 다르지용
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)