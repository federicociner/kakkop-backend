import math
from typing import Dict, List

from django.core.exceptions import ValidationError

from ..models.game import Game
from ..models.player import Player
from ..models.round import Round
from .utilities import find_index


class HannibalGameService:
    def __init__(self):
        self.deck_size = 52

    def calculate_max_hand_size(self, number_of_players: int) -> int:
        return math.floor(self.deck_size / number_of_players)

    def generate_dealers(
        self,
        first_dealer_id: int,
        max_hand_size: int,
        number_of_rounds: int,
        players: List[Dict],
    ) -> List[int]:
        start_index = find_index(players, "id", first_dealer_id)
        players = players[start_index:] + players[:start_index]
        cards = self.get_cards_per_round(max_hand_size, number_of_rounds)
        dealer_index = 0
        dealers = []

        for cards, num in zip(cards, range(1, number_of_rounds + 1)):
            dealers.append(
                {
                    "number_of_cards": cards,
                    "round_number": num,
                    "dealer": players[dealer_index]["player"],
                }
            )
            dealer_index = num % len(players)

        return dealers

    def generate_players(self, game: Game, players_data: List[Dict]) -> None:
        for player_data in players_data:
            Player.objects.create(game=game, **player_data)

    def generate_rounds(self, game: Game) -> None:
        players_query = Player.objects.filter(game=game).order_by("position")
        players = [{"id": p.id, "player": p} for p in players_query]
        first_dealer_id = players_query.get(game=game, is_first_dealer=True).id

        # Calculate number of rounds and generate dealers array
        number_of_players = len(players)
        number_of_rounds = self.get_number_of_rounds(number_of_players)
        max_hand_size = self.calculate_max_hand_size(number_of_players)
        dealers = self.generate_dealers(
            first_dealer_id, max_hand_size, number_of_rounds, players
        )

        # Create Round objects based on dealers array
        for obj in dealers:
            Round.objects.create(
                game=game,
                dealer=obj["dealer"],
                number=obj["round_number"],
                number_of_cards=obj["number_of_cards"],
            )

        # Update number of rounds in Game object
        game.number_of_rounds = len(dealers)
        game.save()

    def get_cards_per_round(
        self, max_hand_size: int, number_of_rounds: int
    ) -> List[int]:
        starting_cards = (max_hand_size * 2) - number_of_rounds + 1
        first = [i for i in range(starting_cards, max_hand_size + 1)]
        second = [i for i in range(max_hand_size, 0, -1)]

        return first + second

    def get_number_of_rounds(
        self, number_of_players: int, starting_cards: int = 2
    ) -> int:
        max_hand_size = self.calculate_max_hand_size(number_of_players)

        if starting_cards > max_hand_size:
            raise ValidationError("Starting cards exceeds maximum hand size.")

        return (max_hand_size * 2) - starting_cards + 1
