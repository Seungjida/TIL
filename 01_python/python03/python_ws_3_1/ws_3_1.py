number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


increase_user()
print(f'현재 가입 된 유저 수 : {number_of_people}')
