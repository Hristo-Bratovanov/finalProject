from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from employees.models import Employee
from projects.models import Project

UserModel = get_user_model()


class EmployeeModelTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(email="user@example.com", password="pass123")
        self.project = Project.objects.create(
            name="Test Project",
            project_photo=SimpleUploadedFile(
                "photo.jpg", b"fakeimagecontent", content_type="image/jpeg"
            ),
            user=self.user
        )

    def test_create_employee_with_required_fields(self):
        emp = Employee.objects.create(
            employee_name="John Doe",
            phone_number="+123456789",
            job_level="Junior",
            user=self.user
        )
        self.assertEqual(str(emp), "John Doe")
        self.assertEqual(emp.user, self.user)

    def test_employee_can_have_projects(self):
        emp = Employee.objects.create(
            employee_name="Jane Smith",
            phone_number="+987654321",
            job_level="Senior",
            user=self.user
        )
        emp.projects.add(self.project)
        self.assertIn(self.project, emp.projects.all())

    def test_job_level_choices(self):
        emp = Employee.objects.create(
            employee_name="Level Test",
            phone_number="+111111111",
            job_level="Team Leader",
            user=self.user
        )
        self.assertEqual(emp.job_level, "Team Leader")


class EmployeeViewsTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(email="user@example.com", password="pass123")
        self.client.login(email="user@example.com", password="pass123")

    def test_employee_details_view(self):
        emp = Employee.objects.create(
            employee_name="Peter Clark",
            phone_number="+123456789",
            job_level="Senior",
            user=self.user
        )
        response = self.client.get(reverse("employee-details", kwargs={"pk": emp.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Peter Clark")

