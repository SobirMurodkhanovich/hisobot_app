import pandas as pd
from django.db.models import Sum, F
from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import default_storage

from .serializers import StudentSerializers
from .models import Student


# Create your views here.


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


class StudentSumView(APIView):

    def get(self, request):
        total_should_give = Student.objects.aggregate(total=Sum('should_give'))['total']
        total_give = Student.objects.aggregate(total=Sum('gave'))['total']
        half_pay = Student.objects.filter(payment_types="half_payment").count()
        full_pay = Student.objects.filter(payment_types="full_payment").count()
        teacher_pay = Student.objects.filter(payment_types="payment_of_the_teacher").count()
        center_pay = Student.objects.filter(payment_types="payment_of_the_center").count()
        debt = total_should_give - total_give

        # Return the result as a JSON response
        return Response({
            "Yig'ilishi kerak": total_should_give,
            "Yig'ildi": total_give,
            "Qarz": debt,
            "Yarim to'lov": half_pay,
            "To'liq to'lov": full_pay,
            "Faqat o'qituvchiga to'lov": teacher_pay,
            "Faqat markazga to'lov: ": center_pay,
        })


class UploadExcelView(APIView):
    def post(self, request):
        file = request.FILES['file']
        file_name = default_storage.save(file.name, file)
        file_path = default_storage.path(file_name)

        try:
            data = pd.read_excel(file_path)
            for _, row in data.iterrows():
                student_data = {
                    'full_name': row["full_name"],
                    'teacher': row["teacher"],
                    'should_give': row['should_give'],
                    'gave': row['gave'],
                    'payment_types': row["payment_types"],
                }
                serializer = StudentSerializers(data=student_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'status': 'success'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class DebtorListView(APIView):
    def get(self, request):
        debtors = Student.objects.filter(gave__lt=F('should_give'))
        serializer = StudentSerializers(debtors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TotalAmountOwedView(APIView):
    def get(self, request):
        total_owed = Student.objects.filter(gave__lt=F('should_give')).aggregate(
            total_owed=Sum(F('should_give') - F('gave'))
        )['total_owed']

        total_owed = total_owed or 0

        return Response({"Yig'ilishi kerak": total_owed}, status=status.HTTP_200_OK)


class StudentsByTeacherView(APIView):
    def get(self, request, teacher):
        students = Student.objects.filter(teacher=teacher)
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
