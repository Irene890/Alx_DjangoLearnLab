from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Using a class-based view (ListView) is the modern, more efficient way to handle lists of objects.
class PostListView(ListView):
    """
    View to display a list of all published blog posts.
    """
    model = Post # Tells the view what model to query
    template_name = 'blog/index.html' # Specifies the template to use
    context_object_name = 'posts' # Name of the variable to loop over in the template (e.g., {% for post in posts %})
    ordering = ['-published_date'] # Explicitly order by newest first
    paginate_by = 10 # Optional: Add pagination for larger blogs

# You can also use a simple function-based view if preferred:
# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/index.html', context)