# 원주율
circumference = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# 반지름
radius = 15

circumference_format = '원주율 : '
radius_format = '반지름 : '
round_format = '원의 둘레 : '
area_format = '원의 넓이 : '

print(f'{circumference_format} {circumference}')
print(f'{radius_format} {radius}')
print(f'{round_format} {radius * 2 * circumference}')
print(f'{area_format} {radius**2*circumference}')