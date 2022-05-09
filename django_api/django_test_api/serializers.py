from pyexpat import model

#from attr import fields
from rest_framework import routers, serializers, viewsets
from django_test_api.models import Projects, Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'eid', 'sys_name', 'characteristics')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('name', 'classification', 'language')