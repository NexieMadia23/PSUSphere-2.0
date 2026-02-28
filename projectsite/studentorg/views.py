from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Organization, OrgMember, Student, College, Program
from .forms import OrganizationForm, OrgMemberForm, StudentForm, CollegeForm, ProgramForm

# --- HOME ---
class HomePageView(TemplateView):
    template_name = 'home.html'

# --- ORGANIZATION ---
class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = Organization.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return queryset

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

# --- ORGMEMBER ---
class OrgMemberList(ListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'orgmember_list.html'
    paginate_by = 5

    def get_queryset(self):
        # Optimized with select_related for student and organization
        queryset = OrgMember.objects.select_related('student', 'organization')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(student__firstname__icontains=query) | 
                Q(student__lastname__icontains=query) |
                Q(organization__name__icontains=query)
            )
        return queryset

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmember-list')

# --- STUDENT ---
class StudentList(ListView):
    model = Student
    context_object_name = 'student'
    template_name = 'student_list.html'
    paginate_by = 5

    def get_queryset(self):
        # Optimized to reach Program AND College in one go
        queryset = Student.objects.select_related('program__college')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(lastname__icontains=query) | 
                Q(firstname__icontains=query) | 
                Q(student_id__icontains=query) |
                Q(program__prog_name__icontains=query) |
                Q(program__college__college_name__icontains=query)
            )
        return queryset

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

# --- COLLEGE ---
class CollegeList(ListView):
    model = College
    context_object_name = 'college'
    template_name = 'college_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = College.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(college_name__icontains=query) # Note: matching your model field name 'college_name'
            )
        return queryset

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

# --- PROGRAM ---
class ProgramList(ListView):
    model = Program
    context_object_name = 'program'
    template_name = 'program_list.html'
    paginate_by = 5

    def get_queryset(self):
        # Optimized with select_related for college
        queryset = Program.objects.select_related('college')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(prog_name__icontains=query) | Q(college__college_name__icontains=query)
            )
        return queryset

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')