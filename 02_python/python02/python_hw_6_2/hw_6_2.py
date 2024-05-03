# 아래 함수를 수정하시오.
def remove_duplicates_to_set(arr):
    count_list = [0 for i in range(10)]
    for index in arr:
        count_list[index] += 1
    result = [num for num in range(len(count_list)) if count_list[num] >= 1] 
    return set(result)

result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
