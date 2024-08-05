from rest_framework import generics, parsers
from .serializers import UserSerializer
from .models import User

class CreateUserAPI(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class RetreiveUserAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]