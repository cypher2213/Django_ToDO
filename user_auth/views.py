from django.contrib.auth.models import User
from rest_framework import  viewsets, permissions,generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer,EmailTokenSerializer
# Create your views here.
   
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    
class LoginView(TokenObtainPairView):
    serializer_class = EmailTokenSerializer
