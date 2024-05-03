from django.shortcuts import render
from bs4 import BeautifulSoup
from selenium import webdriver
from .models import Article, Query

# Create your views here.
def get_data(keyword):
    url = f'http://www.google.com/search?q={keyword}'

    #  동적인 페이지는 request 요청(정적페이지 전용)으로 정상적으로 가져올 수 없다
    # response = requests.get(url)
    # print(response.text)

    # 크롬 브라우저가 열림
    # 이 때, 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome()
    driver.get(url)
    # 열린 페이지 소스들을 받아온다.
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = []
    # 각 게시물을 가져오자!
    # 공통적으로 div 태그 + g 클래스
    g_list = soup.select('div.g')
    for g in g_list:
        print(g)
        # 요소 안에서 ~ ~ ~클래스를 가진 특정 요소 선택
        title = g.select_one(".~.~.~")
        # 요소가 존재한다면
        if title is not None:
            results.append(title.text)
    
    return results


def crawling(request):
    keyword = "탕수육"
    titles =  get_data(keyword)
    for title in titles:
        # get_or_create: 있다면 조회, 없다면 생성
        # 기존에 이미 저장된 것들이면 pass
        # 1. keyword 저장
        # 2. article 저장
        query_obj, created_query = Query.objects.get_or_create(keyword=keyword)
        article, created_article = Article.objects.get_or_create(query=query_obj,title=title)

    # return render ~~