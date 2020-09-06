from django.test import TestCase

from ..models import BaseUser
from ..serializers import UserSerializer


class UserSerializerTest(TestCase):
    def setUp(self):
        self.user_attributes = {
            "email": "testuser@test.com",
            "first_name": "Foo",
            "last_name": "Bar",
            "password": "sometestpassword123",
        }

        self.user = BaseUser.objects.create(**self.user_attributes)
        self.serializer = UserSerializer(instance=self.user)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertCountEqual(
            data.keys(), ["id", "email", "first_name", "last_name"]
        )
        self.assertEqual(data["first_name"], "Foo")
        self.assertEqual(data["last_name"], "Bar")
