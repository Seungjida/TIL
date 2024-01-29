number_of_people = 0
number_of_book = 100

many_user = []
info = {}

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user():
    increase_user()
    for i in range(len(name)):
        many_user.append({'name': name[i], 'age': age[i], 'address':address[i]})
        info[name[i]] = age[i]
        print(f'{name[i]}님 환영합니다!')

def create_user_info():
    # 여기 이상해
    info = dict(map(lambda user: (user['name'],user['age']), many_user))

    list(map(lambda user_info: rental_book(*user_info), info.items()))

# 아 언패킹 다시 공부해라
def rental_book(name, age):
    rental_book_count = age // 10
    decrease_book(rental_book_count)
    print(f'{name}님이 {rental_book_count}권의 책을 대여하였습니다.')

def decrease_book(rental_once_count):
    global number_of_book
    number_of_book -= rental_once_count
    print(f'남은 책의 수 : {number_of_book}')

create_user()
create_user_info()