
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from books.models import Library ,Category
from .models import Author


def author_view(request):
    # Get all authors initially
    authors = Author.objects.all()

    # Get filter parameters from the GET request
    category_name = request.GET.get('category_name', '')
    category_id = request.GET.get('category', '')
    library_name = request.GET.get('library_name', '')
    library_id = request.GET.get('library', '')

    # Apply category filter if a category is selected
    if category_id:
        authors = authors.filter(books__category__id=category_id)

    # Apply library filter if a library is selected
    if library_id:
        authors = authors.filter(books__library__id=library_id)

    # Fetch all categories and libraries to populate the filter dropdowns
    categories = Category.objects.all()
    libraries = Library.objects.all()

    # Prepare a list of authors with their book counts based on the filters
    authors_with_book_count = []
    for author in authors:
        # Calculate book count using the book_count method with category filter if applied
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
    # Retrieve the author object by its ID
    author = get_object_or_404(Author, pk=author_id)

    # Get all categories and libraries for filtering
    categories = Category.objects.all()
    libraries = Library.objects.all()

    # Filter books based on category and library
    books = author.books.all()

    # Apply filters if they are provided in the GET request
    category_filter = request.GET.get('category')
    library_filter = request.GET.get('library')

    if category_filter:
        books = books.filter(category_id=category_filter)

    if library_filter:
        books = books.filter(library_id=library_filter)

    return render(request, 'author_detail.html', {
        'author': author,
        'books': books,
        'categories': categories,
        'libraries': libraries,
        'category_filter': category_filter,
        'library_filter': library_filter,
    })