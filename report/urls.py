from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, StudentSumView, DebtorListView, \
    TotalAmountOwedView, StudentsByTeacherView, UploadExcelView

router = DefaultRouter()
router.register(r'student', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('students/plan/', StudentSumView.as_view(), name='student-sum-should-give'),
    path('students/debtors/', DebtorListView.as_view(), name='debtor-list'),
    path('students/total-amount-owed/', TotalAmountOwedView.as_view(), name='total-amount-owed'),
    path('teachers/<str:teacher>/students/', StudentsByTeacherView.as_view(), name='students-by-teacher'),
    path('upload/', UploadExcelView.as_view()),
]
