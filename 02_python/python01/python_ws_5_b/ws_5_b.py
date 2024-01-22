data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.
for data in data_1:
    if data.isupper() or (data == ' '):
        print(data, end='')
print()

data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.
find_nae = data_2.find('내')
arr.append(find_nae)
find_him = data_2.find('힘')
arr.append(find_him)
find_deul = data_2.find('들')
arr.append(find_deul)
find_da = data_2.find('다')
arr.append(find_da)
print(arr)

arr.sort()
print(arr)

for index in arr:
    print(data_2[index], end='')
print()