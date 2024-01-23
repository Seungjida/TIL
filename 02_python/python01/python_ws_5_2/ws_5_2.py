# set()쓴 방법
# def remove_duplicates(target_list):
#     new_lst = list(set(target_list))

#     return new_lst

# for문으로 요소들 확인한 방법
def remove_duplicates(target_list):
    new_lst = []
    for element in target_list:
        if element not in new_lst:
            new_lst.append(element)
    return new_lst



result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)