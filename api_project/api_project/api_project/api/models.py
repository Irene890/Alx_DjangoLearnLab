from django.db import models

# Step 4: Define a simple Book Model for our API
class Book(models.Model):
    """
    A simple model representing a book.
    Used for the initial API setup.
    """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']