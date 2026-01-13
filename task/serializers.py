from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    status = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        return Task.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.status = validated_data.get('status', instance.status)
        instance.created_at = validated_data.get('created_at',instance.created_at)
        instance.updated_at = validated_data.get('updated_at',instance.updated_at)
        instance.save()
        return instance
    
    class Meta:
        model = Task