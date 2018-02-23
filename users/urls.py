from django.urls import path, include
from users.views import (
    IndexView,
    PostRegView,
    VerifyEmailView,
    VerificationCodeView,
    HomeView,
    ProfileView,
    TestView,
    )

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post-registration/', PostRegView.as_view(), name='post-reg'),
    path('verify-email/' ,VerifyEmailView.as_view(), name='verify-email'),
    path('verication-code/', VerificationCodeView.as_view(), name='verication-code'),
    path('home/', HomeView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('test/', TestView.as_view(), name='test')
]