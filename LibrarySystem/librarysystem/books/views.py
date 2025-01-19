from django.shortcuts import render

def book_view(request):
    return render(request, 'books.html')
# Create your views here.
