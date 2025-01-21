from django.db import models
from authors.models import Author  
from library.models import Library  

class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name


class Book(models.Model):
    book_name = models.CharField(max_length=255)
    author = models.ForeignKey('authors.Author', on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='books')
    library = models.ForeignKey('library.Library', on_delete=models.CASCADE, related_name='books')
    copies = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.book_name

    def author_name(self):
        return self.author.author_name

    def category_name(self):
        return self.category.category_name

