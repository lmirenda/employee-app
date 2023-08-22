from rest_framework import generics

from employees.models import Employee
from employees.permissions import UserOrReadOnly
from employees.serializers.employee_serializer import EmployeeSerializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [UserOrReadOnly]


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
