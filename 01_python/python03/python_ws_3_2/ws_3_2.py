number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1


def create_user(name, age, address):
    increase_user()
    user_info = {'name': name, 'age':age, 'address':address }
    print(f'{user_info["name"]}님 환영합니다!')
    return user_info

def current_users_number():
    print(f'현재 가입 된 유저 수 : {number_of_people}')

current_users_number()
users_info = create_user('홍길동', 30, '서울')
print(users_info)
current_users_number()