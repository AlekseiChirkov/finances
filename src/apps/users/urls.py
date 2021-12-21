from django.urls import path

from apps.users import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.UserSignUpFormView.as_view(), name='signup'),
    path('login/', views.UserLoginFormView.as_view(), name='login'),
    path('profile/<int:pk>', views.UserProfileView.as_view(), name='profile'),
]