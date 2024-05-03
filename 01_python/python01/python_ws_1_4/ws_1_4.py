# 원주율
PI = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# 반지름
radius = 15

PI_is = '원주율 : '
radius_is = '반지름 : '
perimeter = '원의 둘레 : '
area = '원의 넓이 : '

print(f'{PI_is} {PI}')
print(f'{radius_is} {radius}')
print(perimeter, radius * 2 * PI)
print(area, radius * radius * PI)