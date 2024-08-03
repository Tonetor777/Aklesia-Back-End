from rest_framework import generics
from .serializers import UserSerializer
from .models import User

class CreateUserAPI(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
