import datetime

from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    birthday = models.DateField()
    enrollment_date = models.DateField()

    def __str__(self):
        return self.name

    def has_birthday_in_range(self, start_date, days):
        return start_date <= self.birthday <= start_date + datetime.timedelta(days=days)

    def has_enrollment_in_range(self, start_date, days):
        return start_date <= self.enrollment_date <= start_date + datetime.timedelta(days=days)
