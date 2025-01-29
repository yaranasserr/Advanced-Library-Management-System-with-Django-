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
library_locations = [
    (37.423021, -122.083739),  # Googleplex (Google Headquarters), Mountain View, CA, USA
    (40.748817, -73.985428),   # Empire State Building, New York City, USA
    (51.507351, -0.127758),    # Big Ben, London, UK
    (48.856613, 2.352222),     # Eiffel Tower, Paris, France
    (34.052235, -118.243683),  # Hollywood Sign, Los Angeles, CA, USA
    (39.904202, 116.407395),  ] # Forbidden City, Beijing, China

def seed_libraries(n):
    for i in range(n):
        # Select a location from predefined ones
        lat, lon = library_locations[i % len(library_locations)]
        
        Library.objects.create(
            library_name=fake.company(),
            address=fake.address(),
            latitude=lat,
            longitude=lon
        )

def seed_authors(n):
    for _ in range(n):
        Author.objects.create(
            author_name=fake.name()
        )

def seed_categories():
    categories = [
       "Adventure", "Crime", "Horror", "Self-help", "Poetry"
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
    seed_libraries(6)  # Add 5 libraries
    seed_authors(10)   # Add 10 authors
    seed_categories()  # Add predefined categories
    seed_books(20)     # Add 20 books
    print("Database seeded successfully!")

if __name__ == "__main__":
    run_seed()
