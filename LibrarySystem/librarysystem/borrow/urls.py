from django.urls import path
from . import views

urlpatterns = [
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('unborrow/<int:borrow_id>/', views.unborrow_book, name='unborrow_book'),
]
