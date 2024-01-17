# 아래 함수를 수정하시오.
def add_numbers(parm1, parm2):
    return parm1 + parm2


# 수정한 add_numbers() 함수를 호출하시오.
arg1, arg2 = map(int, input().split())
print(f'{arg1}과 {arg2}를 인자로 넘긴 경우,\n{add_numbers(arg1, arg2)}')