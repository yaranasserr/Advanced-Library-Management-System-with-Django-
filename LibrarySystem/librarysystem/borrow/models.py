from django.db import models

from django.contrib.auth.models import User
from books.models import Book

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrows')
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE, related_name='borrows')
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()
    penalty = models.FloatField(default=0)

    def __str__(self):
        return self.book.book_name

    def user_name(self):
        return self.user.username

    def book_name(self):
        return self.book.book_name

    def author_name(self):
        return self.book.author.author_name

    def category_name(self):
        return self.book.category.category_name

    def library_name(self):
        return self.book.library.library_name

    def copies(self):
        return self.book.copies