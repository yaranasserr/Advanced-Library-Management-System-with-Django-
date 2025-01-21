from django.contrib import admin
from .models import Library

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('library_name', 'address', 'latitude', 'longitude')  
    search_fields = ('library_name', 'address')  
