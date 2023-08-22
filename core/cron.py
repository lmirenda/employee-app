from django.utils import timezone

from employees.email.employee_events_email import send_employee_event_email
from employees.models import Employee


def notify_upcoming_employee_events():
    today = timezone.now().date()
    anniversary_list = []
    birthday_list = []

    upcoming_birthdays = Employee.objects.birthdays_within_date_range(str(today), 1)
    upcoming_anniversaries = Employee.objects.enrollments_within_date_range(
        str(today), 1
    )

    if upcoming_birthdays.exists():
        birthdays = list(upcoming_birthdays.values_list("name", "birthday"))
        birthday_list = [{"name": item[0], "amount": (today.year - item[1].year)} for item in birthdays]

    if upcoming_anniversaries.exists():
        anniversaries = list(upcoming_birthdays.values_list("name", "birthday"))
        anniversary_list = [{"name": item[0], "amount": (today.year - item[1].year)} for item in anniversaries]

    if not upcoming_birthdays and not upcoming_anniversaries:
        return

    email_list = ["example1@example.com", "example2@example.com"]
    send_employee_event_email(anniversary_list, birthday_list, email_list)
