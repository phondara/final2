from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=255)
bio = models.TextField(blank=True, null=True)


def __str__(self):
    return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


def __str__(self):
    return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ManyToManyField(Category, related_name='books')
    published_date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


def __str__(self):
    return self.title


class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(blank=True, null=True)