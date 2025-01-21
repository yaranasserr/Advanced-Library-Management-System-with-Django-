

from django.shortcuts import render
from .models import Library
from books.models import Category, Book
from authors.models import Author

def library_view(request):

    category_filter = request.GET.get('category', None)
    author_filter = request.GET.get('author', None)

    libraries = Library.objects.all()

    if category_filter:
        libraries = libraries.filter(books__category__id=category_filter)

    if author_filter:
        libraries = libraries.filter(books__author__id=author_filter)

  
    categories = Category.objects.all()
    authors = Author.objects.all()

    context = {
        'libraries': libraries.distinct(),  
        'categories': categories,
        'authors': authors,
        'category_filter': category_filter,
        'author_filter': author_filter,
    }

    return render(request, 'library.html', context)
