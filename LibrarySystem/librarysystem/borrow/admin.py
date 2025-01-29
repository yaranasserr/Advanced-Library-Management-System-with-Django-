from django.contrib import admin

# Register your models here.
from .models import Borrow

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'borrow_date', 'return_date') 
    search_fields = ('book__book_name', 'user__username', 'borrow_date', 'return_date')
