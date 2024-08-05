from django.urls import path
from . import views

urlpatterns = [
    path('user/create/', views.CreateUserAPI.as_view()),
    path('user/<int:id>/', views.RetreiveUserAPI.as_view()),
]