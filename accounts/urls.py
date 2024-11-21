from django.urls import path
from .views import signup, login_view, dashboard
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
]


urlpatterns += [
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]


