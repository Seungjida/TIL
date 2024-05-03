from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

# 어떤 게시글인지 상관없음. 걍 모두 조회 또는 새로운 게시물 생성
# 이 데코레이터는 drf의 규칙 !!
@api_view(['GET', 'POST'])
def article_list(request):
    # 일단 조회 !
    if request.method == 'GET':
        articles = Article.objects.all()
        # 유연한 데이터(serialized data) 객체로 변환
        # 다중 데이터임, 모든 articles를 조회하는데 저 필드만 조회하는 거임
        serializer = ArticleListSerializer(articles, many=True)
        # 실제 데이터만 추출
        return Response(serializer.data)
    
    # 요청 종류가 2개가 아니니까 else보다는 elif 이렇게 해야 정확해
    elif request.method == 'POST':
        # 새로운 게시글은 모든 필드에 대한 유효성 검사를 해야하니까 ArticleSerializer 호출
        # 첫번째 인자는 인스턴스여야하는데 아니니까 data=로 키워드 인자 ㄱㄱ
        serializer = ArticleSerializer(data=request.data)
        # modelform instance의 메서드 is_valid랑 다른데 이름만 같음
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 성공했을 때 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 실패했을 때 400, serializer.is_valid 때문에 error가 들어감
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 어떤 게시글에 대해서 처리를 해야하는지 봐야함 !!
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # 하나의 article의 모든 필드를 조회
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        # 단일 데이터라서 many 옵션 빼
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        # 수정을 부분적으로 할 수도 있으니까 partial 옵션을 true, 아니면 매번 전체 데이터를 다 보냄
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        # 실패했을 때 400 리턴 반복되니까 귀찮, raise_exception 옵션하면 자동적으로 예외 처리됨 굿~!
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
