import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_data(keyword):
    url = f'http://www.google.com/search?q={keyword}'

    # 크롬 브라우저가 열림
    # 이 때, 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome()
    driver.get(url)
    # 열린 페이지 소스들을 받아온다.
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 검색 결과 개수
    # result-stats id 사용
    # result_stats = soup.select_one('#result-stats')
    # print(result_stats.text)

    # 각 게시물을 가져오자!
    # 공통적으로 div 태그 + g 클래스
    g_list = soup.select('div.g')
    for g in g_list:
        print(g)
        # 요소 안에서 ~ ~ ~클래스를 가진 특정 요소 선택
        title = g.select_one(".~.~.~")
        # 요소가 존재한다면
        if title is not None:
            print('제목 = ', title.text)

keyword = "탕수육"
get_data(keyword)