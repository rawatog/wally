from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def unauthenticated_user(view_func):
    """Decorator to prevent authenticated users from accessing a view."""
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Change 'home' to your desired URL name
        return view_func(request, *args, **kwargs)
    return wrapper
