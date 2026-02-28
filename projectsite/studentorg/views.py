from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView # Combined these
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from studentorg.models import Organization
from studentorg.forms import OrganizationForm

class HomePageView(TemplateView):
    template_name = "home.html"

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

# Cleaned OrganizationUpdateView
class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')