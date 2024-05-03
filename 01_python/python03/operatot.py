# 빈문자열은 False도 아니고 True도 아님
print('' == False)
print('' == True)

# 조건문에서 빈문자열은 False로 암묵적 형변환
if '':
    print('빈문자열은... 빈문자열?')
else:
     print('아무일도 벌어지지 않음')
three = ''
four = '4'
if three and four:
     print('3과 4')
else:
     print('실패')