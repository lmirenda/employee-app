import requests
from django.utils import timezone
from datetime import timedelta

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def check_holidays_view(request):
    today = timezone.now().date()
    api_key = "1d591a6b7bd840e89ab2e862ad770933"
    country_code = "US"
    base_url = "https://holidays.abstractapi.com/v1/"

    holidays_in_range = []
    for i in range(0, 3):

        params = {
            "api_key": api_key,
            "country": country_code,
            "year": today.year,
            "month": today.month,
            "day": today.day,
        }

        response = requests.get(url=base_url, params=params)

        holidays_data = response.json()
        holidays_in_range.append(i)

        if holidays_data != [] and response.status_code == 200:
            for holiday in holidays_data:
                holidays_in_range.append(holiday)
        today = today + timedelta(days=1)

    return Response(holidays_in_range)
