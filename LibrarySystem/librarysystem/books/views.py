# views.py
from django.shortcuts import render
from .models import Book, Category, Library, Author
from borrow.models import Borrow

def book_view(request):
    categories = Category.objects.all()
    libraries = Library.objects.all()
    authors = Author.objects.all()

    books = Book.objects.all()

    # Filter books based on GET parameters
    if request.GET.get('category_name'):
        books = books.filter(category__category_name__icontains=request.GET['category_name'])
    elif request.GET.get('category'):
        books = books.filter(category__id=request.GET['category'])

    if request.GET.get('library_name'):
        books = books.filter(library__library_name__icontains=request.GET['library_name'])
    elif request.GET.get('library'):
        books = books.filter(library__id=request.GET['library'])

    if request.GET.get('author_name'):
        books = books.filter(author__author_name__icontains=request.GET['author_name'])
    elif request.GET.get('author'):
        books = books.filter(author__id=request.GET['author'])

    # Check if the logged-in user has already borrowed each book
    borrowed_books = {}
    if request.user.is_authenticated:
        user_borrowed_books = Borrow.objects.filter(user=request.user)
        for borrow in user_borrowed_books:
            borrowed_books[borrow.book.id] = True

    return render(request, 'books.html', {
        'books': books,
        'categories': categories,
        'libraries': libraries,
        'authors': authors,
        'user': request.user,
        'borrowed_books': borrowed_books,  
    })
