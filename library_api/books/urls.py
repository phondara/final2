# books/urls.py
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, CategoryViewSet, BookViewSet, BorrowRecordViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'books', BookViewSet, basename='book')
router.register(r'borrows', BorrowRecordViewSet, basename='borrow')

urlpatterns = router.urls
