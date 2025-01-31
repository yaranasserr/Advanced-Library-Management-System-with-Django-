
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from books.models import Library ,Category
from .models import Author
from borrow.models import Borrow
from django.utils.translation import gettext as _


def author_view(request):

    authors = Author.objects.all()


    category_name = request.GET.get('category_name', '')
    category_id = request.GET.get('category', '')
    library_name = request.GET.get('library_name', '')
    library_id = request.GET.get('library', '')

   
    if category_id:
        authors = authors.filter(books__category__id=category_id)

    
    if library_id:
        authors = authors.filter(books__library__id=library_id)

    
    categories = Category.objects.all()
    libraries = Library.objects.all()

    authors_with_book_count = []
    for author in authors:
       
        author.book_count_value = author.book_count(category_id if category_id else None)
        authors_with_book_count.append(author)

    authors_with_book_count.sort(key=lambda author: author.book_count_value, reverse=True)


    return render(request, 'authors.html', {
        'authors_with_book_count': authors_with_book_count,
        'categories': categories,
        'libraries': libraries,
        'category_name': category_name,
        'library_name': library_name,
    })

def author_detail(request, author_id):
    
    author = get_object_or_404(Author, pk=author_id)

    
    categories = Category.objects.all()
    libraries = Library.objects.all()

   
    books = author.books.all()

    category_filter = request.GET.get('category')
    library_filter = request.GET.get('library')

    if category_filter:
        books = books.filter(category_id=category_filter)

    if library_filter:
        books = books.filter(library_id=library_filter)

     # Check if the logged-in user has already borrowed each book
    borrowed_books = {}
    if request.user.is_authenticated:
        user_borrowed_books = Borrow.objects.filter(user=request.user)
        for borrow in user_borrowed_books:
            borrowed_books[borrow.book.id] = True

   




    return render(request, 'author_detail.html', {
        'author': author,
        'books': books,
        'categories': categories,
        'libraries': libraries,
        'category_filter': category_filter,
        'library_filter': library_filter,
        'user': request.user,
        'borrowed_books': borrowed_books,  
    })