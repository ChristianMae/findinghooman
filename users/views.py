from django.shortcuts import render
from django.views.generic import TemplateView, View
from users.forms import (
    PreRegistrationForm, 
    LoginForm,
    )

class IndexView(TemplateView):
    template_name= 'user/index.html'


class PostRegView(TemplateView):
    template_name ='user/post_registration.html'


class VerifyEmailView(TemplateView):
    template_name = 'user/verify_email.html'


class VerificationCodeView(TemplateView):
    template_name = 'user/verification_code.html'


class HomeView(TemplateView):
    template_name = 'finder/home.html'


class ProfileView(TemplateView):
    template_name = 'finder/profile.html'


class TestView(TemplateView):
    template_name = 'user/test.html'