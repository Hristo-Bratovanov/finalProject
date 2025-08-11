from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from project_pictures.models import ProjectPicture
from projects.models import Project

UserModel = get_user_model()


class ProjectModelTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(email="user@example.com", password="pass123")
        self.project = Project.objects.create(
            name="Test Project",
            project_photo=SimpleUploadedFile(
                "photo.jpg", b"fakeimagecontent", content_type="image/jpeg"
            ),
            user=self.user
        )
        self.picture = ProjectPicture.objects.create(
            picture=SimpleUploadedFile(
                "pic1.jpg", b"fakepiccontent", content_type="image/jpeg"
            ),
            project=self.project,
            user=self.user
        )

    def test_create_project_with_required_fields(self):
        prj = Project.objects.create(
            name="Test Project",
            project_photo=SimpleUploadedFile(
                "photo.jpg", b"fakeimagecontent", content_type="image/jpeg"
            ),
            user=self.user
        )
        self.assertEqual(str(prj), "Test Project")
        self.assertEqual(prj.user, self.user)

    def test_project_can_have_pictures(self):
        prj = Project.objects.create(
            name="Test Project",
            project_photo=SimpleUploadedFile(
                "photo.jpg", b"fakeimagecontent", content_type="image/jpeg"
            ),
            user=self.user
        )
        prj.pictures.add(self.picture)
        self.assertIn(self.picture, prj.pictures.all())


class ProjectViewsTests(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(email="user@example.com", password="pass123")

    def test_project_details_view(self):
        prj = Project.objects.create(
            name="Test Project",
            project_photo=SimpleUploadedFile(
                "photo.jpg", b"fakeimagecontent", content_type="image/jpeg"
            ),
            user=self.user
        )
        response = self.client.get(reverse("project-details", kwargs={"project_slug": prj.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Project")
