from django.shortcuts import render
from .models import Book
from .forms import SearchForm

# Existing view
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Additional secure search view
def search_books(request):
    form = SearchForm(request.GET)
    books = []
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})