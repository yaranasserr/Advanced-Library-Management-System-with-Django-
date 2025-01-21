import os
import django
from faker import Faker
from random import randint, choice

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'librarysystem.settings')  # Replace with your project's name
django.setup()

# Import your models
from library.models import Library
from authors.models import Author
from books.models import Book, Category

# Initialize Faker
fake = Faker()

def seed_libraries(n):
    for _ in range(n):
        Library.objects.create(
            library_name=fake.company(),
            address=fake.address(),
            latitude=fake.latitude(),
            longitude=fake.longitude()
        )

def seed_authors(n):
    for _ in range(n):
        Author.objects.create(
            author_name=fake.name()
        )

def seed_categories():
    categories = [
        "Fiction", "Non-fiction", "Mystery", "Science Fiction", "Fantasy", 
        "Romance", "Thriller", "Biography", "Historical Fiction", "Science", 
        "Technology", "Philosophy", "Arts", "Psychology", "Health"
    ]
    for category in categories:
        Category.objects.create(category_name=category)

def seed_books(n):
    authors = list(Author.objects.all())
    categories = list(Category.objects.all())
    libraries = list(Library.objects.all())

    for _ in range(n):
        Book.objects.create(
            book_name=fake.sentence(nb_words=3),
            author=choice(authors),
            category=choice(categories),
            library=choice(libraries),
            copies=randint(1, 20)
        )

def run_seed():
    print("Seeding database...")
    seed_libraries(5)  # Add 5 libraries
    seed_authors(10)   # Add 10 authors
    seed_categories()  # Add predefined categories
    seed_books(20)     # Add 20 books
    print("Database seeded successfully!")

if __name__ == "__main__":
    run_seed()
