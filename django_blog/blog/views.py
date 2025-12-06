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

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileForm
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES or None)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after register (optional)
            messages.success(request, "Registration successful.")
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

@login_required
def profile_view(request):
    if request.method == "POST":
        pform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if pform.is_valid():
            pform.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
    else:
        pform = ProfileForm(instance=request.user.profile)
    return render(request, "blog/profile.html", {"pform": pform})
