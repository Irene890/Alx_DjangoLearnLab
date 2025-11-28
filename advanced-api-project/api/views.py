from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

# ---------------------------------------------------------
# ListView: Retrieve all books
# This view allows ANYONE (authenticated or not) to read data.
# Uses ListAPIView which provides an optimized read-only list.
# ---------------------------------------------------------
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # public read access

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']



# ---------------------------------------------------------
# DetailView: Retrieve a single book by ID
# Allows unauthenticated users to view details.
# ---------------------------------------------------------
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ---------------------------------------------------------
# CreateView: Add a new book
# Only authenticated users can create books.
# Uses CreateAPIView to simplify object creation.
# Custom validation is already defined in BookSerializer.
# ---------------------------------------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Example customization: automatically log the user who submitted the create request.
    def perform_create(self, serializer):
        # This hook gives a chance to modify or log creation behavior.
        print(f"User {self.request.user} created a book.")
        serializer.save()


# ---------------------------------------------------------
# UpdateView: Modify an existing book
# Only authenticated users are allowed.
# The UpdateAPIView uses PATCH/PUT operations.
# ---------------------------------------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Additional customization: log update action
    def perform_update(self, serializer):
        print(f"Book updated by {self.request.user}")
        serializer.save()


# ---------------------------------------------------------
# DeleteView: Remove a book
# Only authenticated users can delete.
# Uses DestroyAPIView for delete operations.
# ---------------------------------------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Optional: customize delete behavior
    def perform_destroy(self, instance):
        print(f"Book '{instance.title}' deleted by {self.request.user}")
        super().perform_destroy(instance)
