from django.shortcuts import render
from rest_framework.views import APIView
from .models import Task
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework import generics, viewsets

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

