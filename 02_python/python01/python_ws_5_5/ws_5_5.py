# 내가 한 거 !!!!!!!!
# pop()이 쓰기 힘들었던 이유는 요소를 pop하고 나면 현재 돌리고 있는
# 반복문의 표현식 또한 영향을 받아서....
# out of range하거나.. 튼 오류가 날 수 있음

# import copy
# # 아래 함수를 수정하시오.
# def even_elements(original_list):
#     odd_list = []
#     even_list = []
#     for element in original_list:
#         if element % 2 != 0:
#             index = original_list.index(element)
#             odd_list.append(original_list.pop(index))
#     even_list.extend(original_list)
#     return even_list

# 다른 코드 참고 !!!!!!!
# while이 pop로 인해 바뀐 arr에 따라 반복문을 실행 
# extend()는 쓰라고 하니까 썼지 굳이 필요없는듯
def even_elements(arr):
    result= []
    tmp = []

    while arr:
        # 0번째 요소를 pop -> pop에 인자를 안넣으면 뒤에서부터 제거
        # -> 리스트의 순서가 바뀔 수 있음.
        element = arr.pop(0)
        if element % 2 == 0:
            tmp.append(element)
    result.extend(tmp)
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
