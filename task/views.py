from django.shortcuts import render
from rest_framework.views import APIView
from .models import Task
from rest_framework.response import Response
from .serializers import TaskSerializer

# Create your views here.
class TaskApiView(APIView):
    
    def get(self,request):
        tasks = Task.objects.all()
        return Response({'tasks':TaskSerializer(tasks,many=True).data})
    
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'message':"Task created successfully",
            'new_task': serializer.data
        })
        
    def put(self,request,*args, **kwargs):
        pk = kwargs.get('pk',None)
        
        if not pk:
            return Response({'message':'Method PUT is not allowed'})
        
        try:
            instance = Task.objects.get(pk=pk)
        except:
            return Response({'message':f'Task with id {pk} is not found'})
        
        serializer = TaskSerializer(data=request.data, instance = instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
            
        return Response({
            'message':'Task updated successfully',
            'task':serializer.data
        })
        