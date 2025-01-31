from django.shortcuts import render
from .models import Library
from users.models import Profile  
from books.models import Category, Book
from authors.models import Author

def library_view(request):
    category_filter = request.GET.get('category', None)
    author_filter = request.GET.get('author', None)

    libraries = Library.objects.all()

    user_profile = None
    if request.user.is_authenticated:
   
        user_profile = request.user.profile  

    if category_filter:
        libraries = libraries.filter(books__category__id=category_filter)

    if author_filter:
        libraries = libraries.filter(books__author__id=author_filter)

    categories = Category.objects.all()
    authors = Author.objects.all()

    library_data = []
    for library in libraries:
        distance = None
        
        if user_profile and user_profile.latitude and user_profile.longitude:
            distance = library.get_distance_from_user(user_profile.latitude, user_profile.longitude)
        library_data.append({
            'library': library,
            'distance': distance
        })

    context = {
        'library_data': library_data,  
        'categories': categories,
        'authors': authors,
        'category_filter': category_filter,
        'author_filter': author_filter,
    }

    return render(request, 'library.html', context)
