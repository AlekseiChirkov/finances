from django.contrib.auth import authenticate, login, get_user_model
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView

from apps.users.forms import UserCreationForm, UserLoginForm


class UserSignUpFormView(FormView):
    """View for users sign up"""

    form_class = UserCreationForm
    template_name = 'pages/users/signup.html'
    success_url = reverse_lazy('finances:account-list')

    def form_valid(self, form):
        """Activate user if signup form valid"""

        user = form.save(commit=False)
        user.is_active = True
        user.save()
        return super(UserSignUpFormView, self).form_valid(form)
    
    def form_invalid(self, form):
        """Process invalid signup form"""

        return super(UserSignUpFormView, self).form_invalid(form)


class UserLoginFormView(FormView):
    """View for users login"""

    form_class = UserLoginForm
    template_name = 'pages/users/login.html'
    success_url = reverse_lazy('finances:account-list')

    def form_valid(self, form):
        """Login user if form is valid"""

        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(username=email, password=password)

        if user is not None and user.is_active:
            login(self.request, user)

        return super(UserLoginFormView, self).form_valid(form)

    def form_invalid(self, form):
        """Process invalid form"""

        return super(UserLoginFormView, self).form_invalid(form)


class UserProfileView(DetailView):
    """User profile view"""

    model = get_user_model()
    template_name = 'pages/users/profile.html'

