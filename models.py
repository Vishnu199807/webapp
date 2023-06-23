from django.db import models
from django.utils.timezone import now


class Book(models.Model):

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    created_date = models.DateTimeField(default=now)
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    book_code = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.FloatField()

    def _str_(self):
        return self.title
class Author(models.Model):
    name = models.CharField(max_length=255)
    birthdate = models.DateField()
    email = models.EmailField()

    def _str_(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=255)

    def _str_(self):
        return self.name
class Genre(models.Model):
    name = models.CharField(max_length=255)

    def _str_(self):
        return self.name

class BookManager(models.Manager):
    def available_books(self):
        return self.filter(is_available=True)

class Book(models.Model):

    objects = BookManager()