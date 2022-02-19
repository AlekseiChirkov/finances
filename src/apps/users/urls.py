from django.urls import path
from django.contrib.auth.views import LogoutView

from apps.users import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.UserSignUpFormView.as_view(), name='signup'),
    path('login/', views.UserLoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>', views.UserProfileView.as_view(), name='profile'),
    path('password-change/', views.UserPasswordChangeView.as_view(), name='password-change'),
]