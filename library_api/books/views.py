# books/views.py
from rest_framework import viewsets
from .models import Author, Category, Book, BorrowRecord
from .serializers import AuthorSerializer, CategorySerializer, BookSerializer, BorrowRecordSerializer
from .permissions import IsOwnerOrAdmin

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwnerOrAdmin()]
        return super().get_permissions()

class BorrowRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
