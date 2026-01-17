from .models import Task
from .serializers import TaskSerializer, RegisterSerializer, EmailTokenSerializer
from rest_framework import  viewsets, permissions,generics
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get_queryset(self):
       return Task.objects.filter(owner=self.request.user)
   
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    
class LoginView(TokenObtainPairView):
    serializer_class = EmailTokenSerializer

