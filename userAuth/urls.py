from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('user/token', TokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view())
]