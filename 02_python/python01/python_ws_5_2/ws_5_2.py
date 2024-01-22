# 아래 함수를 수정하시오.
def remove_duplicates(target_list):
    new_lst = list(set(target_list))

    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)