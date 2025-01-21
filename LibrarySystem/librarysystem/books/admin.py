from django.contrib import admin
from .models import Book, Category

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'author', 'category', 'library', 'copies') 
    search_fields = ('book_name', 'author__author_name', 'category__category_name', 'library__library_name') 
    list_filter = ('category', 'library', 'author')  
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)  
    search_fields = ('category_name',) 
