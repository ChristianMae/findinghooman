from django.urls import path, include
from finder.views import (
    HomeView
    )

urlpatterns = [
    path('home/', HomeView.as_view(), ),
]