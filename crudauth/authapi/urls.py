from django.urls import path
from authapi import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'list', views.ListTaskManagerAPIView)
router.register(r'create', views.CreateTaskManagerAPIView)
router.register(r'update', views.UpdateTaskManagerAPIView)
router.register(r'delete', views.DeleteTaksManagerAPIView)

urlpatterns = [
    path("", views.ListTaskManagerAPIView.as_view(), name="tasks_list"),
    path("createTask/", views.CreateTaskManagerAPIView.as_view(), name="task_create"),
    path("updateTask/<int:pk>/", views.UpdateTaskManagerAPIView.as_view(), name="task_update"),
    path("deleteTask/<int:pk>/", views.DeleteTaksManagerAPIView.as_view(), name="task_delete"),
]