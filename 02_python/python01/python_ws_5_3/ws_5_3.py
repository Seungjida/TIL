# 아래 함수를 수정하시오.
def sort_tuple(original_tuple):
    new_tuple = ()
    original_list = list(original_tuple)
    original_list.sort()
    new_tuple = tuple(original_list)
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
