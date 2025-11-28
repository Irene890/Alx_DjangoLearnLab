# Advanced API Project — Views & Permissions

## Overview
This project demonstrates the use of Django REST Framework generic views, custom view behavior, and permission handling for API development.

## View Breakdown
- **BookListView** — Public access, returns all books.
- **BookDetailView** — Public access, returns a book by ID.
- **BookCreateView** — Authenticated users only, creates a new book.
- **BookUpdateView** — Authenticated users only, updates an existing book.
- **BookDeleteView** — Authenticated users only, deletes a book.

## Permissions
- `AllowAny` for read-only views.
- `IsAuthenticated` for write operations.

## Custom Behavior
Each write view overrides:
- `perform_create()`
- `perform_update()`
- `perform_destroy()`

These provide hooks for logging or extending business logic.

## Testing
Use Postman or curl to test all endpoints and verify permissions.

## Query Capabilities

### Filtering
Example:
GET /books/?author=3

### Searching
Full-text search on title and author name:
GET /books/?search=Rowling

### Ordering
Sort by title or publication year:
GET /books/?ordering=-publication_year
