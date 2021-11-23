from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import reverse, redirect
from django.views.generic import FormView

from apps.users.forms import UserCreationForm, UserLoginForm


class UserSignUpFormView(FormView):
    form_class = UserCreationForm
    template_name = 'pages/signup.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()
        return super(UserSignUpFormView, self).form_valid(form)
    
    def form_invalid(self, form):
        return super(UserSignUpFormView, self).form_invalid(form)


class UserLoginFormView(FormView):
    form_class = UserLoginForm
    template_name = 'pages/login.html'
    success_url = '/'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(username=email, password=password)

        if user is not None and user.is_active:
            login(self.request, user)

        return super(UserLoginFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(UserLoginFormView, self).form_invalid(form)
