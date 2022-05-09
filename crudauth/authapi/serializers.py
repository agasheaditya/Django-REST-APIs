from authapi.models import TaskManager
from rest_framework import serializers

class TaskManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskManager
        fields = "__all__"