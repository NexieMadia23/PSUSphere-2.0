from django.contrib import admin
from django.urls import path, include
# Import allauth views specifically to fix the template error
from allauth.account import views as allauth_views 

from studentorg.views import (
    HomePageView, 
    OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView,
    OrgMemberList, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView,
    StudentList, StudentCreateView, StudentUpdateView, StudentDeleteView,
    CollegeList, CollegeCreateView, CollegeUpdateView, CollegeDeleteView,
    ProgramList, ProgramCreateView, ProgramUpdateView, ProgramDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- ALLAUTH URLS (Login, Signup, Socials) ---
    path('accounts/', include('allauth.urls')), 

    # --- ALIASES (Fixed to use Allauth views) ---
    # These prevent "Reverse for 'login' not found" AND "TemplateDoesNotExist"
    path('login/', allauth_views.login, name='login'),
    path('logout/', allauth_views.logout, name='logout'),
    path('signup/', allauth_views.signup, name='signup'),
    
    path('', HomePageView.as_view(), name='home'),
    
    # --- ORGANIZATION URLS ---
    path('organization_list/', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add/', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/edit/<int:pk>/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/delete/<int:pk>/', OrganizationDeleteView.as_view(), name='organization-delete'),

    # --- ORGMEMBER URLS ---
    path('orgmember_list/', OrgMemberList.as_view(), name='orgmember-list'),
    path('orgmember_list/add/', OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmember_list/edit/<int:pk>/', OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmember_list/delete/<int:pk>/', OrgMemberDeleteView.as_view(), name='orgmember-delete'),

    # --- STUDENT URLS ---
    path('student_list/', StudentList.as_view(), name='student-list'),
    path('student_list/add/', StudentCreateView.as_view(), name='student-add'),
    path('student_list/edit/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('student_list/delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),

    # --- COLLEGE URLS ---
    path('college_list/', CollegeList.as_view(), name='college-list'),
    path('college_list/add/', CollegeCreateView.as_view(), name='college-add'),
    path('college_list/edit/<int:pk>/', CollegeUpdateView.as_view(), name='college-update'),
    path('college_list/delete/<int:pk>/', CollegeDeleteView.as_view(), name='college-delete'),

    # --- PROGRAM URLS ---
    path('program_list/', ProgramList.as_view(), name='program-list'),
    path('program_list/add/', ProgramCreateView.as_view(), name='program-add'),
    path('program_list/edit/<int:pk>/', ProgramUpdateView.as_view(), name='program-update'),
    path('program_list/delete/<int:pk>/', ProgramDeleteView.as_view(), name='program-delete'),
]