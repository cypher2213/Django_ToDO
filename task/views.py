from .models import Task
from .serializers import TaskSerializer
from rest_framework import  viewsets, permissions

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get_queryset(self):
       return Task.objects.filter(owner=self.request.user)

