# Create your views here.
from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})