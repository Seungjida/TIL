my_list = ['가', '나', '다', '라']

# 4번 인덱스는 없으니까 오류가 날까?
# 할 수 있는 것과 해도 되는 것은 다르다.
# 슬라이싱으로 범위를 벗어난 경우,
# 예외 처리가 되지 않아서 예상하지 못한
# 상황이 발생 할 수 있다.
print(my_list[2:5])
# 예상과 달리 출력 결과는 ['다', '라'] 였다.
# 범위를 벗어나는 상황 잘 생각하기

print(my_list[4])