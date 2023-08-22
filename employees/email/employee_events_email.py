from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_employee_event_email(anniversaries: list, birthdays: list, emails: list):
    context = {"anniversaries": anniversaries, "birthdays": birthdays}

    email_subject = "Upcoming Employee Events"
    email_body = render_to_string("employee_email_events.txt", context)

    email_message = EmailMessage(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        emails,
    )

    return email_message.send(fail_silently=False)
