from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import BaseUser


class UserTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        user_attributes = {
            "email": "foo@bar.com",
            "first_name": "Foo",
            "last_name": "Bar",
        }
        cls.user = BaseUser.objects.create(**user_attributes)
        cls.user.set_password("bojangles")
        cls.user.save()

    def test_create_user(self):
        url = reverse("register")
        data = {
            "email": "second@bar.com",
            "first_name": "Second",
            "last_name": "User",
            "password1": "waffles42",
            "password2": "waffles42",
        }
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BaseUser.objects.count(), 2)
        self.assertEqual(
            BaseUser.objects.get(first_name="Second").email, "second@bar.com"
        )

    def test_login_user(self):
        url = reverse("login")
        data = {"email": "foo@bar.com", "password": "bojangles"}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertCountEqual(
            response.data.keys(), ["access_token", "refresh_token", "user"]
        )
        self.assertCountEqual(
            response.data["access_token"].keys(), ["expiration", "value"]
        )
        self.assertCountEqual(
            response.data["refresh_token"].keys(), ["expiration", "value"]
        )
        self.assertCountEqual(
            response.data["user"].keys(),
            ["id", "email", "first_name", "last_name"],
        )
