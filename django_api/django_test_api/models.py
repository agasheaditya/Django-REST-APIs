from django.db import models

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=150)
    classification = models.CharField(max_length=150)
    language = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=150)
    eid = models.CharField(max_length=100)
    sys_name = models.CharField(max_length=100)
    characteristics = models.ForeignKey(Projects, on_delete=models.DO_NOTHING)