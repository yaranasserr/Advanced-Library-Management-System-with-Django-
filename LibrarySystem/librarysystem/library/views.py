from django.shortcuts import render

def library_view(request):
    return render(request, 'library.html')

