from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from accounts.forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .models import Complaint

# @login_required
# def home(request):
#     if request.method == 'POST':
#         complaint_text = request.POST.get('complaint')
#         user_type = request.POST.get('user_type')
        
#         if complaint_text and user_type:
#             # Save the complaint to the database
#             Complaint.objects.create(user=request.user, user_type=user_type, complaint_text=complaint_text)
#             messages.success(request, "Your complaint has been submitted successfully.")
#             return redirect('home')
#         else:
#             messages.error(request, "Please fill in all fields.")
    
#     return render(request, 'accounts/home.html')




