from django.db import models


class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    # ManyToManyField - related_name 작성
    # 역참조시 사용하는 manager name을 바꿔줘욤 ~~!
    # 완전 변경! 과거의 이름은 못 쓴데이

    # 대칭 옵션도 있어ㅛㅇ용 !! 동일한 모델을 가리키는 정의에서만 사용~! 아직 안 배움

    doctors = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
