# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include('accounts.urls')),
# ]
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Redirect root URL to login or dashboard
def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to dashboard if logged in
    return redirect('login')  # Redirect to login if not logged in

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include accounts app URLs
    path('', home_redirect, name='home'),  # Root URL redirects to appropriate page
]

    