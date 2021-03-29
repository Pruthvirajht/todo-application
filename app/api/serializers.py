from app.models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','task_title','task_description','status']