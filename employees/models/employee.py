from datetime import datetime, timedelta

from django.db import models
from django.db.models import Q


class EmployeeManager(models.Manager):
    def filter_by_date_range(self, field_name, start_date, days):
        start_date_obj = datetime.strptime(start_date, "%d-%m-%Y")

        end_date_obj = start_date_obj + timedelta(days=days)

        if start_date_obj.month == end_date_obj.month:
            date_range_filter = Q(
                **{
                    f"{field_name}__month": start_date_obj.month,
                    f"{field_name}__day__gte": start_date_obj.day,
                    f"{field_name}__day__lte": end_date_obj.day,
                }
            )
        else:
            date_range_filter = (
                Q(
                    **{
                        f"{field_name}__month": start_date_obj.month,
                        f"{field_name}__day__gte": start_date_obj.day,
                    }
                )
                | Q(
                    **{
                        f"{field_name}__month": end_date_obj.month,
                        f"{field_name}__day__lte": end_date_obj.day,
                    }
                )
                | Q(
                    **{
                        f"{field_name}__month__gt": start_date_obj.month,
                        f"{field_name}__month__lt": end_date_obj.month,
                    }
                )
            )

        return date_range_filter

    def birthdays_within_date_range(self, start_date, days):
        return self.get_queryset().filter(
            self.filter_by_date_range("birthday", start_date, days)
        )

    def enrollments_within_date_range(self, start_date, days):
        return self.get_queryset().filter(
            self.filter_by_date_range("enrollment_date", start_date, days)
        )


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    birthday = models.DateField()
    enrollment_date = models.DateField()

    def __str__(self):
        return self.name

    objects = EmployeeManager()
