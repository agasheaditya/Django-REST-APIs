from django.urls import include, path
from rest_framework import routers
from django_test_api.views import EmployeeViewset, ProjectViewset

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewset)
router.register(r'project', ProjectViewset)

urlpatterns = [
    path('', include(router.urls)),
]