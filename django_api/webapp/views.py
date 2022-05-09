from django.shortcuts import render
from django.views.generic import View
from webapp.services import get_employee_data, get_project_data

# Create your views here.
class DashboardsView(View):
    template_name = "index.html"
    def get(self, request, *args, **kwargs):      
        context = {
            'emp' : get_employee_data(),
            'projects' : get_project_data()
        }
        return render(request, "index.html", context=context)
        #return context
        