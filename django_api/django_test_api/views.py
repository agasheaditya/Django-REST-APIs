from django.shortcuts import render
from rest_framework import viewsets


from django_test_api.serializers import EmployeeSerializer, ProjectSerializer
from django_test_api.models import Employee, Projects

# Create your views here.

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer


