from datetime import datetime

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from employees.models import Employee
from employees.serializers.employee_serializer import EmployeeSerializer


class AnniversaryFilterListView(ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get(
            "start_date", datetime.now().strftime("%Y-%m-%d")
        )
        days = int(self.request.query_params.get("days", 0))

        return Employee.objects.enrollments_within_date_range(start_date, days)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        modified_data = []
        for item in serializer.data:
            item["event_type"] = "anniversary"
            modified_data.append(item)

        return Response(modified_data)
