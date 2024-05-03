from django.db import models


class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


# 외래키 삭제
class Patient(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


# 중개모델 작성
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'


# 코드 예시
doctor1 = Doctor.objects.create(name='allie')
patient1 = Patient.objects.create(name='carol')

# 예약이 만드는 건 좀 이상.. 말 자체가~ 안 되는 건 아님
# 장고에선 ManyToManyField로 중개모델을 자동으로 생성
Reservation.objects.create(doctor=doctor1, patient=patient1)

# 1의 입장이 N을 역참조 해야징
doctor1.reservation_set.all()
patient1.reservation_set.all()

patient2 = Patient.objects.create(name='duke')
Reservation.objects.create(doctor=doctor1, patient=patient2)
