from django.db import models

from django.contrib.auth.models import User
from books.models import Book  
class BookNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    notified = models.BooleanField(default=False)  # To track if the user has been notified

    def __str__(self):
        return f"{self.user.first_name} - {self.book.book_name}"