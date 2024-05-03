# 아래 클래스를 수정하시오.
class StringRepeater:
    def repeat_string(self, repeats, rep_string):
        while repeats:
            print(rep_string)
            repeats -= 1


repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
