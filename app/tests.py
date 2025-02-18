from django.test import TestCase
from datetime import date
from decimal import Decimal
from .models import Book, Author

# Create your tests here.

class AuthorModelTest(TestCase):
    """
    Class for testing author model
    """
    def setUp(self):
        self.author = Author.objects.create(name="Kamil Slimak", age = 30)

    def test_str(self):
        self.assertEqual(str(self.author), "Kamil Slimak")

    def test_age(self):
        self.assertEqual(self.author.age,30)

class BookModelTest(TestCase):
    """
    Class for testing book model
    """
    def setUp(self):
        self.author = Author.objects.create(name="Kamil Slimak", age=30)
        self.book = Book.objects.create(
            title = "Killers Of The Flower Moon",
            author = self.author,
            published_date=date(2004,1,3),
            price = Decimal("10.29")
        )

    def test_book_str(self):
        self.assertEqual(str(self.book), "Killers Of The Flower Moon")

    def test_book_author_relationship(self):
        self.assertEqual(self.book.author, self.author)

    def test_book_published_date(self):
        self.assertEqual(self.book.published_date, date(2004, 1, 3))

    def test_book_price(self):
        self.assertEqual(self.book.price, Decimal("10.29"))