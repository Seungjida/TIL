title = '딕셔너리 활용하기'
# 아래에 코드를 작성하시오.

data = {'과목': 'Python', '구분': '실습', '단계': 2, '문제번호': 3251, '이름': None, '일차': 22}
print(data)

data['단계'] = str(data['단계']) + '단계'
data['이름'] = title
data['일차'] -= 20
print(data)
