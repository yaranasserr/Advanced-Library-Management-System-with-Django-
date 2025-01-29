from celery import shared_task
from django.core.mail import send_mail
from datetime import date, timedelta


@shared_task
def send_due_date_reminders():
    from borrow.models import Borrow
    today = date.today()
    three_days_later = today + timedelta(days=3)

    borrowings = Borrow.objects.filter(return_date__range=(today, three_days_later))

    for borrow in borrowings:
        user = borrow.user
        book = borrow.book
        days_left = (borrow.return_date - today).days  

        send_mail(
            subject="Library Reminder: Book Due Soon",
            message=f"Dear {user.username},\n\nYour borrowed book '{book.title}' is due in {days_left} days. "
                    f"Please return it on time to avoid penalties.\n\nThank you!",
            from_email="your-library@example.com",
            recipient_list=[user.email],
        )
