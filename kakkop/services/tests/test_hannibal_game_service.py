from django.core.exceptions import ValidationError
from django.test import TestCase

from users.models import BaseUser

from ... import constants
from ...models.game import Game
from ...models.player import Player
from ...models.round import Round
from ..hannibal import HannibalGameService


class HannibalGameServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        users = [
            {
                "email": "user1@bar.com",
                "first_name": "Stevie Ray",
                "last_name": "Vaughn",
            },
            {
                "email": "user2@bar.com",
                "first_name": "Jimi",
                "last_name": "Hendrix",
            },
            {
                "email": "user3@bar.com",
                "first_name": "Jimmy",
                "last_name": "Page",
            },
        ]

        for user_data in users:
            BaseUser.objects.create(**user_data)

    def setUp(self):
        self.first_user = BaseUser.objects.get(email="user1@bar.com")
        self.second_user = BaseUser.objects.get(email="user2@bar.com")
        self.third_user = BaseUser.objects.get(email="user3@bar.com")
        self.service = HannibalGameService()

        game_data = {
            "creator": self.first_user,
            "game_type": constants.HANNIBAL,
        }
        self.game = Game.objects.create(**game_data)

    def test_correct_number_of_rounds(self):
        number_of_rounds = self.service.get_number_of_rounds(4)

        self.assertEqual(number_of_rounds, 25)

        with self.assertRaises(ValidationError) as e:
            self.service.get_number_of_rounds(4, starting_cards=14)

        self.assertEqual(
            e.exception.message, "Starting cards exceeds maximum hand size.",
        )

    def test_correct_cards_dealt_per_round(self):
        max_hand_size = 13
        number_of_rounds = 25
        cards = self.service.get_cards_per_round(
            max_hand_size, number_of_rounds
        )

        self.assertEqual(len(cards), 25)
        self.assertEqual(cards[0], 2)
        self.assertEqual(cards[-1], 1)
        self.assertEqual(cards.count(max_hand_size), 2)

    def test_players_generated_correctly(self):
        players = [
            {"user": self.first_user, "position": 0, "is_first_dealer": False},
            {"user": self.second_user, "position": 1, "is_first_dealer": True},
            {"user": self.third_user, "position": 2, "is_first_dealer": False},
        ]
        self.service.generate_players(self.game, players)

        self.assertEqual(Player.objects.count(), 3)
        self.assertEqual(
            Player.objects.get(user=self.second_user).is_first_dealer, True
        )
        self.assertCountEqual(
            list(Player.objects.values_list("user", flat=True)),
            list(BaseUser.objects.values_list("id", flat=True)),
        )

    def test_rounds_generated_correctly(self):
        players = [
            {"user": self.first_user, "position": 0, "is_first_dealer": False},
            {"user": self.second_user, "position": 1, "is_first_dealer": True},
            {"user": self.third_user, "position": 2, "is_first_dealer": False},
        ]
        self.service.generate_players(self.game, players)
        self.service.generate_rounds(self.game)

        self.assertEqual(Round.objects.count(), 33)
        self.assertEqual(self.game.number_of_rounds, 33)
        self.assertEqual(
            Round.objects.get(number=1).dealer,
            Player.objects.get(user=self.second_user),
        )
        self.assertEqual(Round.objects.get(number=1).number_of_cards, 2)
        self.assertEqual(Round.objects.get(number=33).number_of_cards, 1)
