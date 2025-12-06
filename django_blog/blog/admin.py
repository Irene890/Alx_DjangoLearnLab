from django.contrib import admin
from .models import Post

# Register the Post model so it appears in the Django Admin interface.
admin.site.register(Post)