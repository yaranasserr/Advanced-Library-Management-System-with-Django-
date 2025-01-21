from django.shortcuts import render
from .models import Book, Category, Library, Author

# def book_view(request):
#     # Fetch all books from the database
#     books = Book.objects.all()

#     # Pass the books to the template
#     return render(request, 'books.html', {'books': books})

def book_view(request):
    
    categories = Category.objects.all()
    libraries = Library.objects.all()
    authors = Author.objects.all()

    books = Book.objects.all()


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

    return render(request, 'books.html', {
        'books': books,
        'categories': categories,
        'libraries': libraries,
        'authors': authors,
    })

