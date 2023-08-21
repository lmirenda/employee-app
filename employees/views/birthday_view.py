from datetime import datetime

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from employees.models import Employee
from employees.serializers.employee_serializer import EmployeeSerializer


class BirthdayFilterListView(ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        # Get start_date and days from query parameters
        start_date = self.request.query_params.get(
            "start_date", datetime.now().strftime("%Y-%m-%d")
        )
        days = int(self.request.query_params.get("days", 0))
        # Call the custom manager method to get the filtered queryset
        queryset = Employee.objects.birthdays_within_date_range(start_date, days)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Manipulate serialized data to include the "event_type" field
        modified_data = []
        for item in serializer.data:
            item["event_type"] = "birthday"
            modified_data.append(item)

        return Response(modified_data)
