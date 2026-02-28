from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember
import random

class Command(BaseCommand):
    help = "Create initial data for the application"

    def handle(self, *args, **kwargs):
        # Ensure we have base data first
        self.ensure_base_data()
        
        # Create related data
        self.create_organization(10)
        self.create_students(50)
        self.create_membership(20) # Increased to 20 for better testing

    def ensure_base_data(self):
        """Ensures at least one College and Program exist before seeding others."""
        college, created = College.objects.get_or_create(college_name="Default College")
        if created:
            self.stdout.write(self.style.WARNING("Created a default College."))
        
        program, created = Program.objects.get_or_create(
            program_name="Default Program", 
            college=college
        )
        if created:
            self.stdout.write(self.style.WARNING("Created a default Program."))

    def create_organization(self, count):
        fake = Faker()
        colleges = College.objects.all()
        for _ in range(count):
            words = [fake.word().capitalize() for _ in range(2)]
            org_name = f"{' '.join(words)} Organization"
            Organization.objects.create(
                organization_name=org_name,  # Matches your admin.py field
                college=random.choice(colleges),
                description=fake.sentence(),
            )
        self.stdout.write(self.style.SUCCESS(f"{count} organizations created successfully."))

    def create_students(self, count):
        fake = Faker("en_PH")
        programs = Program.objects.all()
        for _ in range(count):
            Student.objects.create(
                student_id=f"{fake.random_int(2020, 2025)}-{fake.random_int(1, 8)}-{fake.random_number(digits=4)}",
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.last_name(),
                program=random.choice(programs),
            )
        self.stdout.write(self.style.SUCCESS(f"{count} students created successfully."))

    def create_membership(self, count):
        fake = Faker()
        students = Student.objects.all()
        orgs = Organization.objects.all()
        
        created_count = 0
        while created_count < count:
            student = random.choice(students)
            org = random.choice(orgs)
            
            # Prevent duplicate memberships
            obj, created = OrgMember.objects.get_or_create(
                student=student,
                organization=org,
                defaults={'date_joined': fake.date_between(start_date="-2y", end_date="today")}
            )
            if created:
                created_count += 1
                
        self.stdout.write(self.style.SUCCESS(f"{count} memberships created successfully."))