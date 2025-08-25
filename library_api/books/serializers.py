from rest_framework import serializers
from .models import Author, Category, Book, BorrowRecord
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
fields = ['id', 'username', 'email']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    uthor_id = serializers.PrimaryKeyRelatedField(
    queryset=Author.objects.all(), source='author', write_only=True
)
category = CategorySerializer(many=True, read_only=True)
category_ids = serializers.PrimaryKeyRelatedField(
queryset=Category.objects.all(), many=True, source='category', write_only=True
)


class Meta:
    model = Book
    fields = ['id', 'title', 'author', 'author_id', 'category', 'category_ids', 'published_date', 'created_by']
    read_only_fields = ['created_by']


def create(self, validated_data):
    categories = validated_data.pop('category')
    book = Book.objects.create(**validated_data)
    book.category.set(categories)
    return book


class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = '__all__'