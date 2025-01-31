from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.author_name

    def book_count(self, category=None):
        # If a category filter is provided, count only books in that category
        if category:
            return self.books.filter(category=category).count()
        return self.books.count()   
