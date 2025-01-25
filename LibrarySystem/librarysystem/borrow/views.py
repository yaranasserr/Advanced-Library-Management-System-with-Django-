
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from books.models import Book
from .models import Borrow
from datetime import timedelta

from datetime import timedelta
from django.utils import timezone

@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(id=book_id)
    
    if book.copies > 0:
        # Reduce the number of available copies
        book.copies -= 1
        book.save()

        # Calculate return date (e.g., 7 days from today)
        return_date = timezone.now().date() + timedelta(days=30)

        borrow = Borrow.objects.create(
            user=request.user,
            book=book,
            borrow_date=timezone.now().date(),  #
            return_date=return_date, 
            penalty=0  
        )
        borrow.save()

        return redirect('dashboard')
    else:
      
        return render(request, 'books/no_copies_available.html', {'book': book})



@login_required
def unborrow_book(request, borrow_id):
    borrow = Borrow.objects.get(id=borrow_id, user=request.user)
    
    # You can also handle the return date, penalty, etc. here.
    borrow.delete()  # Delete the borrow record when the user returns the book
    
    # Redirect to dashboard after unborrowing
    return redirect('dashboard')
