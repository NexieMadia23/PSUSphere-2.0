from django.shortcuts import render
from django.views.generic.list import ListView
from studentorg.models import Organization

template_name = "home.html" 

class HomePageView(ListView):
    model = Organization
    # Using 'object_list' is standard for pagination, 
    # but we will set context_object_name to organizations for clarity
    context_object_name = 'organizations' 
    template_name = "home.html"
    paginate_by = 5

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5
