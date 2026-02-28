from django.contrib import admin
from django.urls import path
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('organization_list/', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    
    # Notice the <int:pk>/ here. This is required for UpdateView.
    path('organization_list/edit/<int:pk>/', OrganizationUpdateView.as_view(), name='organization-update'),
]