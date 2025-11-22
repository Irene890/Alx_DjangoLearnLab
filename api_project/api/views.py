from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# -----------------------------
# 1. ListAPIView (previous task)
# -----------------------------
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# -----------------------------
# 2. ViewSet for CRUD operations
# -----------------------------
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
