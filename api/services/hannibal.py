import math
from typing import List


class HannibalGameService:
    def __init__(self):
        self.deck_size = 52

    def get_number_of_rounds(
        self, number_of_players: int, starting_cards: int = 2
    ) -> int:
        max_hand_size = math.floor(self.deck_size / number_of_players)

        if starting_cards > max_hand_size:
            raise ValueError("Starting cards cannot exceed maximum hand size.")

        return (max_hand_size * 2) - starting_cards + 1

    def generate_dealer_order(
        self, players: List[int], first_dealer: int
    ) -> List[int]:
        pass
