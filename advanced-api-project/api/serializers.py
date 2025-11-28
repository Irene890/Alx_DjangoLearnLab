from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# BookSerializer:
# Serializes the Book model and includes custom validation
# to ensure publication_year is not a future year.
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    # Custom field-level validation for publication_year
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


# AuthorSerializer:
# Serializes the Author model and nests BookSerializer
# to include all related books.
#
# Using the related name `books` from the ForeignKey,
# we dynamically serialize all books belonging to the author.
class AuthorSerializer(serializers.ModelSerializer):

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
