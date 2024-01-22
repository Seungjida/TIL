# 라이브러리: 남들이 만들어놓은 코드를 가져다가 쓰자!
# 데이터를 가져오는 python 라이브러리(패키지) : requests
# 파이썬 패키지 관리 : pip
    # 설치 : pip install <패키지 이름>
    # 목록 확인 : pip list

# 내 코드에 다른 패키지를 추가
import requests
import pprint

api_key = '37422f8554bb34455b7f149cb33bd8b2'
# 서울의 위도
lat = 37.56
# 서울의 경도
lon = 126.97

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
data = requests.get(url).json()
print(data)

pprint.pprint(data)

# data['weather']
# dta.get('weather')