from django.urls import path

from employees.views.employee_views import EmployeeList, EmployeeDetail

urlpatterns = [
    path("/", EmployeeList.as_view()),
    path("/<int:pk>/", EmployeeDetail.as_view()),
]
