from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherViewSet, StudentViewSet, StudentSumView, HalfPaidStudentsView, DebtorListView, \
    TotalAmountOwedView, StudentsByTeacherView

router = DefaultRouter()
router.register(r'teacher', TeacherViewSet)
router.register(r'student', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('students/total-should-give/', StudentSumView.as_view(), name='student-sum-should-give'),
    path('students/half-paid/', HalfPaidStudentsView.as_view(), name='half-paid-students'),
    path('students/debtors/', DebtorListView.as_view(), name='debtor-list'),
    path('students/total-amount-owed/', TotalAmountOwedView.as_view(), name='total-amount-owed'),
    path('teachers/<int:teacher_id>/students/', StudentsByTeacherView.as_view(), name='students-by-teacher'),
]
