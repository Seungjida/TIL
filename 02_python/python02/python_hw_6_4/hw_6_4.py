# 아래 함수를 수정하시오.
def add_item_to_dict(my_dict, *items):
    new_dict = my_dict.copy()
    new_dict[items[0]] = items[1]

    return new_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
