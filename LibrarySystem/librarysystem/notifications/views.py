from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404 , redirect
from .models import BookNotification
from books.models import Book
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# from .tasks import send_email


@login_required
def notify_when_available(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    user = request.user

    # Step 1: Check if the user has already requested notification for this book
    if not BookNotification.objects.filter(user=user, book=book).exists():
        BookNotification.objects.create(user=user, book=book)

    # Step 2: Check if there are available copies of the book
    books_with_available_copies = Book.objects.filter(copies__gt=0)

    # Step 3: Notify users about available books
    for book in books_with_available_copies:
        users_to_notify = BookNotification.objects.filter(book=book, notified=False)

        for notification in users_to_notify:
            user = notification.user

            subject = f"Book '{book.book_name}' is now available"
            html_message = render_to_string('book_available_email.html', {
                'user': user,
                'book': book
            })
            plain_message = f"Hello {user.first_name},\n\nThe book '{book.book_name}' is now available in the library.\n\nThank you for using our library service!"

            # Send the email notification
            send_mail(
                subject, 
                plain_message, 
                settings.DEFAULT_FROM_EMAIL, 
                [user.email], 
                html_message=html_message,
                fail_silently=False
            )

            # Mark the notification as notified
            notification.notified = True
            notification.save()

    # After sending emails, render a success page with the success message
    success_message = f"You will be notified when the book '{book.book_name}' is available!"
    return render(request, 'notification_sent.html', {'success_message': success_message})

    

# def notify_when_available(request):
#     books_with_available_copies = Book.objects.filter(copies__gt=0)
    
#     for book in books_with_available_copies:
#         users_to_notify = BookNotification.objects.filter(book=book, notified=False)

#         for notification in users_to_notify:
#             user = notification.user

#             subject = f"Book '{book.book_name}' is now available"
#             html_message = render_to_string('book_available_email.html', {
#                 'user': user,
#                 'book': book
#             })
#             plain_message = f"Hello {user.first_name},\n\nThe book '{book.book_name}' is now available in the library.\n\nThank you for using our library service!"

#             # Send the email
#             send_mail(
#                 subject, 
#                 plain_message, 
#                 settings.DEFAULT_FROM_EMAIL, 
#                 [user.email], 
#                 html_message=html_message,
#                 fail_silently=False
#             )

#             notification.notified = True
#             notification.save()

#     # After sending emails, you can render a success page or redirect to a list of books.
#     success_message = "Notifications have been sent to users about available books."
#     return render(request, 'notification_sent.html', {'success_message': success_message})



def send_borrow_confirmation(user, book, return_date):
    subject = f"Book Borrowed: {book.book_name}"
    html_message = render_to_string('borrow_confirmation_email.html', {
        'user': user,
        'book': book,
        'return_date': return_date
    })
    plain_message = f"Hello {user.first_name},\n\nYou have successfully borrowed the book '{book.book_name}'. The expected return date is {return_date}.\n\nThank you for using our library service!"

    send_mail(
        subject,
        plain_message,  
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        html_message=html_message,  
        fail_silently=False
    )
    




# Create your views here.

# def notify_when_available(request, user_id, book_id):
#     user = get_object_or_404(User, id=user_id)
#     book = get_object_or_404(Book, id=book_id)
    
#     # Call your email notification logic
#     subject = f"Book: {book.book_name} is now available"
#     html_message = render_to_string('book_available_email.html', {'user': user, 'book': book})
#     plain_message = f"Hello {user.first_name},\n\nThe book '{book.book_name}' is now available in the library.\n\nThank you for using our library service!"
    
#     send_mail(subject, plain_message, settings.DEFAULT_FROM_EMAIL, [user.email], html_message=html_message, fail_silently=False)

#     return render(request, 'notification_sent.html', {'user': user, 'book': book})

# def say_hello(request):
#     send_email.delay("Hello from Celery!")
#     return render(request, 'notfication_sent.html')