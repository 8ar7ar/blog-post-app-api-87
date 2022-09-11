from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testUser", email="test@gmail.com", password="secret_password_Test"
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title="A Good Test Title",
            body="Good Test Body Content",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testUser")
        self.assertEqual(self.post.title, "A Good Test Title")
        self.assertEqual(self.post.body, "Good Test Body Content")
        self.assertEqual(str(self.post.title), "A Good Test Title")
