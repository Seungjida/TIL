# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        self.user_data['이름'] = None
        self.user_data['나이'] = None 
    
        try:
            print("이름을 입력하세요 :", end=' ')
            self.user_data['이름'] = input()
    
            print("나이를 입력하세요 :", end=' ')
            self.user_data['나이'] = int(input())

        except ValueError:
            print("나이는 숫자로 입력해야 합니다.")


    def display_user_info(self):
        if self.user_data['이름'] != None and self.user_data['나이'] != None:
            print("사용자 정보 :")
            for key, value in self.user_data.items():
                print(f'{key} : {value}')
        else:
            print("사용자 정보가 입력되지 않았습니다.")


user = UserInfo()
user.get_user_info()
user.display_user_info()


# 바보 같은 이승지 걍 입력받은 값을 따로 변수에 저장부터해놓고, 딕셔너리에 키와 벨류 추가하면 됮않아.. 굳이 왜 None 쓴거임?
# 그러면 if self.user_data만 해도 되니잔하아암너러 러ㅏ ㅏ바봐보ㅗ바ㅗ바바바ㅗ바ㅏ봐봐