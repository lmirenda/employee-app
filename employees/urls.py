from django.urls import path

from employees.views.anniversary_view import AnniversaryFilterListView
from employees.views.birthday_view import BirthdayFilterListView
from employees.views.employee_holiday_view import check_holidays_view
from employees.views.employee_views import EmployeeList, EmployeeDetail

urlpatterns = [
    path("", EmployeeList.as_view()),
    path("<int:pk>/", EmployeeDetail.as_view()),
    path("birthday/", BirthdayFilterListView.as_view()),
    path("anniversary/", AnniversaryFilterListView.as_view()),
    path("holidays/", check_holidays_view),
]
