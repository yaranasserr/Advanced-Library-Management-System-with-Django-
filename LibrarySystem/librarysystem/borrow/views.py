from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import Book, Borrow
from django.contrib.auth.decorators import login_required

@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(id=book_id)

    today = timezone.now().date()
    max_return_date = today + timedelta(days=30)

    # Check if the user has already borrowed 3 books
    if Borrow.objects.filter(user=request.user).count() >= 3:
        error_message = 'You cannot borrow more than 3 books at a time.'
        return render(request, 'books.html', {
            'error_message': error_message,
            'is_error': True,
            'book': book, 
            'today': today, 
            'max_return_date': max_return_date,
            'books': Book.objects.all(),
        })

    if request.method == 'POST':
        return_date_str = request.POST.get('return_date')

        if return_date_str:
            return_date = timezone.datetime.strptime(return_date_str, "%Y-%m-%d").date()

            # Ensure the return date is within the 30-day borrowing period
            if return_date > max_return_date:
                error_message = 'Return date cannot be more than 30 days from today.'
                return render(request, 'books.html', {
                    'error_message': error_message,
                    'is_error': True,
                    'book': book, 
                    'today': today, 
                    'max_return_date': max_return_date,
                    'books': Book.objects.all(),
                })

            if book.copies > 0:
                book.copies -= 1
                book.save()

                # Create a borrowing record without setting `remaining_days` and `penalty`
                borrow = Borrow.objects.create(
                    user=request.user,
                    book=book,
                    borrow_date=today,
                    return_date=return_date,
                 
                )
                borrow.save()

                # Success message
                success_message = f'Book "{book.book_name}" has been borrowed successfully.'
                
                return render(request, 'books.html', {
                    'success_message': success_message,
                    'is_success': True,
                    'book': book, 
                    'today': today, 
                    'max_return_date': max_return_date,
                    'books': Book.objects.all(),
                })
            else:
                error_message = 'No copies available.'
                return render(request, 'books.html', {
                    'error_message': error_message,
                    'is_error': True,
                    'book': book, 
                    'today': today, 
                    'max_return_date': max_return_date
                })
        else:
            error_message = 'Please select a return date.'
            return render(request, 'books.html', {
                'error_message': error_message,
                'is_error': True,
                'book': book, 
                'today': today, 
                'max_return_date': max_return_date
            })
    
    return render(request, 'books.html', {
        'book': book, 
        'today': today, 
        'max_return_date': max_return_date
    })


@login_required
def unborrow_book(request, borrow_id):
    borrow = Borrow.objects.get(id=borrow_id, user=request.user)
    book = borrow.book
    
    
    book.copies += 1
    book.save()

    # Optionally, you can handle the return date, penalty, etc. here.

    borrow.delete()

    
    return redirect('dashboard')

