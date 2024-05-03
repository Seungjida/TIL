from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)

'''
Nested_relationships !! 
응답 받는 데이터를 더욱 추가 ~~(재구성)
'''

class ArticleSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content',)
            # read_only_fields = ('article',)

    # 역참조 매니저는 fields에 없으니까 역참조 관련 데이터를 응답받으려면 이렇게(comment_set 역참조 이름 !!! 바꾸면 바꾼 걸로 !!!) 넣어줘야함
    # 게시글 조회시 댓글 필드를 유효성 검사하지 않으니까..!
    # 1 -> N 역참조니까 단일 데이터가 아니다ㅣ!
    comment_set = CommentDetailSerializer(read_only=True, many=True)

    # 응답 데이터에 새로운 필드 작성 !!!
    # source : 필드의 값을 채우는 데 사용할 속성의 이름
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    # 외래키에 대한 정보를 보여주는 serializer인데 위에 거는 너무 자세히 보여주니까 입맛에 맞게 새로 만듦
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    
    # article(참조 대상)을 덮어쓴다.
    # 응답 데이터 재구성~ 이것도 serializer하면 됨
    article = ArticleTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # 읽기 전용 필드, 필드가 기본값(특정 필드를 추가하지 않은 경우)일 때 적용.. 지금은 안 됨
        # read_only_fields = ('articles',)