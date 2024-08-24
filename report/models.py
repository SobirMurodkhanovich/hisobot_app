from django.db import models


class Student(models.Model):
    type_payment = (
        ('half_payment', 'HALF_PAYMENT'),
        ('full_payment', 'FULL_PAYMENT'),
        ('payment_of_the_teacher', 'PAYMENT_OF_THE_TEACHER'),
        ('payment_of_the_center', 'PAYMENT_OF_THE_CENTER'),
    )
    full_name = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    should_give = models.IntegerField()  # berishi kerak
    gave = models.IntegerField(default=0)  # berdi
    payment_types = models.CharField(max_length=50, choices=type_payment)

    def __str__(self):
        return f'Student: {self.full_name}// Teacher: {self.teacher.full_name}'
