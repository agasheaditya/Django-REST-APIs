from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from authapi.models import TaskManager
from authapi.serializers import TaskManagerSerializer

# Create your views here.

#  listdown all records 
class ListTaskManagerAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TaskManager.objects.all()
    serializer_class = TaskManagerSerializer

# create new records
class CreateTaskManagerAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TaskManager.objects.all()
    serializer_class = TaskManagerSerializer

# update existing records using primary key index id
class UpdateTaskManagerAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TaskManager.objects.all()
    serializer_class = TaskManagerSerializer

# delete existing records using primary key index id
class DeleteTaksManagerAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TaskManager.objects.all()
    serializer_class = TaskManagerSerializer
