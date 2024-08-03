from django.urls import path
from . import views

urlpatterns = [
    path('user/create/', views.CreateUserAPI.as_view()),
]