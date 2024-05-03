import requests
from bs4 import BeautifulSoup

'''
requests: HTTP 요청을 보내고 응답을 받을 수 있는 모듈
BeautifulSoup: HTML 문서에서 원하는 데이터를 추출하는데 사용되는 파이선 라이브러리
Selenium: 웹 애플리케이션을 테스트하고 자동화하기 위한 파이썬 라이브러리
'''
url = 'https://quotes.toscrape.com/tag/love/'

# 1. 다운로드 - url을 이용해서, HTML이 담긴 자료를 받아와야 함
response = requests.get(url)

# request가 완벽하게 동일한 것을 받아오는 것은 아니다!

# html문서를 text 형태로 확인
html_text = response.text

# .text는 str type(HTML text)
print(type(html_text))

# 문자열 파싱은 코드로 짜기 복잡하다
# 라이브러리를 쓰자
# 저기 두번째 인자는 html문자를 파싱한다는 뜻
# 파싱은 주어진 문자를 해석하고 그 문자의 구조를 이해하여 사용자가 필요로 하는 정보를 추출하는 과정
soup = BeautifulSoup(html_text, 'html.parser')
# bs4.BeautifulSoup class가 출력됨
print(type(soup))


# BeautifulSoup4 요소 선택 메서드 종류 !!!

# 1. find
# - 첫 번째 태그를 가진 요소를 검색
main = soup.find('a')
print(main)
# 첫 번째 태그의 글자만 필요하다면!
print(main.text)

# 2. find_all
# - 해당 태그를 가진 모든 요소를 검색
a_tags = soup.find_all('a')
# 리스트 형태로 반환
print(a_tags)

# 3. select_one
# - css 선택자(. # 태그 등)를 사용하여 요소를 검색
# 선택자가 일치하는 첫 번째 글

# span 태그로도 검색이 가능하지만 인용구라는 내용은 text class로 지정되어 있으므로 class를 통한 검색(특정할 수 있는 것)이 더 옳다!
word = soup.select_one('.text')
print(f'첫 번째 글 = {word}')

# 4. select
# - css 선택자로 여러개를 선택, 선택자가 일치하는 모든 인용구를 검색하여 리스트 형태로 출력
words = soup.select('.text')
for w in words:
    print(f'글 : {w.text}')