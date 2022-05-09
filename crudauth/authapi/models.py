from statistics import mode
from django.db import models

# Create your models here.
class TaskManager(models.Model):
    taskName = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_created=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.taskName