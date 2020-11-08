import logging
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

LOGGER = logging.getLogger(__file__)

User = get_user_model()


class Command(BaseCommand):
    args = ""
    help = "Create a set of pre-defined users for testing."

    def _create_users(self):
        User.objects.create_superuser(
            email="admin@test.com",
            first_name="Jiminy",
            last_name="Cricket",
            password="password123",
        )

        users = [
            {
                "email": "user1@test.com",
                "first_name": "McDonald",
                "last_name": "Trump",
                "password": "testing123",
            },
            {
                "email": "user2@test.com",
                "first_name": "Bear",
                "last_name": "Grylls",
                "password": "testing1234",
            },
            {
                "email": "user3@test.com",
                "first_name": "Bob",
                "last_name": "The Burger",
                "password": "testing12345",
            },
        ]

        for user in users:
            User.objects.create_user(
                user["email"], user["first_name"], user["last_name"], user["password"]
            )

        LOGGER.info("Successfully created test users.")

    def handle(self, *args, **options):
        self._create_users()
