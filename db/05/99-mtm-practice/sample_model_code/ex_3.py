from django.db import models


class Doctor(models.Model):
    # ManyToManyField 여기에서 작성해보까?
    # 기능은 같은데 참조와 역참조 형태를 어디서 작성하냐에 따라 결정됨(그냥 생각하기 편한 위치에 두자!)
    # doctors = models.ManyToManyField(Doctor)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    # ManyToManyField 작성
    # 작성한 곳(patient)에 물리적인 필드가 만들어지지는 않음
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


# Reservation Class 주석 처리


# 코드 예시
doctor1 = Doctor.objects.create(name='allie')
patient1 = Patient.objects.create(name='carol')
patient2 = Patient.objects.create(name='duke')

# 서로 종속된 관계가 아니다.
# patient가 doctor 참조
patient1.doctors.add(doctor1)
patient1.doctors.all()
# 역참조
doctor1.patient_set.all()

doctor1.patient_set.add(patient2)
doctor1.patient_set.all()
patient2.doctors.all()
patient1.doctors.all()

# 삭제
doctor1.patient_set.remove(patient1)
doctor1.patient_set.all()
patient1.doctors.all()

# 삭제
patient2.doctors.remove(doctor1)
patient2.doctors.all()
doctor1.patient_set.all()
