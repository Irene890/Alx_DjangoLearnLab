from django.db import models

# Author model stores basic information about an author.
# This model has a one-to-many relationship with Book,
# meaning one author can write multiple books.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model stores details about books.
# The 'author' field creates the relationship to Author using ForeignKey.
# Each book belongs to exactly one author.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

