from django.db import models


class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    # 대신 through 옵션을 추가하여 add, remove 편리하게 쓸 수 있음
    # 중개모델 자동생성하면서 Reservation과 비교하여 없는 필드 넣는 거임
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# 예약 정보에 간단한 정보 말고 더 많은 정보들을 포함하고 싶다...! 어쩔 수 없이 클래스 만들어야 함
# db에 생기겠지ㅏ !!!
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'


# 코드 예시
doctor1 = Doctor.objects.create(name='allie')
patient1 = Patient.objects.create(name='carol')
patient2 = Patient.objects.create(name='duke')

# 1. Reservation class를 통한 예약 생성
reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
reservation1.save()
# Reservations.objects.create(doctor=doctor1, patient=patient1, symptom='headache')
doctor1.patient_set.all()
patient1.doctors.all()

# 2. Patient 객체를 통한 예약 생성
patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})
doctor1.patient_set.all()
patient2.doctors.all()

doctor1.patient_set.remove(patient1)
patient2.doctors.remove(doctor1)
