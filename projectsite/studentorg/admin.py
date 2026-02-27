from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

# Task A – CollegeAdmin
@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ("college_name", "created_at", "updated_at")
    search_fields = ("college_name",)
    list_filter = ("created_at",)

# Task B – ProgramAdmin
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("prog_name", "college")
    # Search by program name and the related college name (using __)
    search_fields = ("prog_name", "college__college_name")
    list_filter = ("college",)

# Task C – OrganizationAdmin
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "college", "description")
    search_fields = ("name", "description")
    list_filter = ("college",)

# Keep your existing Student and OrgMember logic below...
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "program")
    search_fields = ("lastname", "firstname", "student_id")
    list_filter = ("program",)

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("get_student_full_name", "get_member_program", "organization", "date_joined")
    search_fields = ("student__lastname", "student__firstname", "organization__name")
    list_filter = ("organization", "date_joined")

    @admin.display(description='Student Name', ordering='student__lastname')
    def get_student_full_name(self, obj):
        return f"{obj.student.lastname}, {obj.student.firstname}" if obj.student else "No Student"

    @admin.display(description='Program')
    def get_member_program(self, obj):
        return obj.student.program.prog_name if obj.student and obj.student.program else "N/A"