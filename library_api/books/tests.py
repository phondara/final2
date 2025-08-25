from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author


class AuthorAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")
        self.author_url = reverse('author-list')


def test_create_author(self):
    data = {"name": "J.K. Rowling", "bio": "Author of Harry Potter"}
    response = self.client.post(self.author_url, data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Author.objects.count(), 1)


def test_get_authors(self):
    Author.objects.create(name="George Orwell")
    response = self.client.get(self.author_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertGreaterEqual(len(response.data), 1)