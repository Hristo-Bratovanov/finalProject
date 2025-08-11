from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model

from project_pictures.models import ProjectPicture
from projects.models import Project


UserModel = get_user_model()

class ProjectPictureModelTests(TestCase):

    def setUp(self):
        self.user = UserModel.objects.create_user(
            email="test@example.com",
            password="pass1234"
        )
        self.project = Project.objects.create(
            name="Test Project",
            project_photo=SimpleUploadedFile(
                "photo.jpg", b"fakeimagecontent", content_type="image/jpeg"
            ),
            user=self.user
        )

    def test_project_picture_creation(self):
        picture = ProjectPicture.objects.create(
            picture=SimpleUploadedFile(
                "pic1.jpg", b"fakepiccontent", content_type="image/jpeg"
            ),
            project=self.project,
            user=self.user
        )
        self.assertEqual(picture.project, self.project)
        self.assertTrue(picture.user, self.user)


    def test_deleting_project_deletes_pictures(self):
        ProjectPicture.objects.create(
            picture=SimpleUploadedFile("picdel.jpg", b"img", content_type="image/jpeg"),
            project=self.project,
            user=self.user
        )
        self.project.delete()
        self.assertEqual(ProjectPicture.objects.count(), 0)

    def test_reverse_relation_from_project(self):
        picture = ProjectPicture.objects.create(
            picture=SimpleUploadedFile("picrev.jpg", b"img", content_type="image/jpeg"),
            project=self.project,
            user=self.user
        )
        self.assertEqual(self.project.pictures.count(), 1)
        self.assertEqual(self.project.pictures.first(), picture)

