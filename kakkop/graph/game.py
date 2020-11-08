import logging

import graphene
from django.db.transaction import atomic
from graphene_django import DjangoObjectType

from kakkop import constants
from kakkop.graph.player import PlayerInput
from kakkop.graph.round import RoundType
from kakkop.graph.user import UserType
from kakkop.models.game import Game
from kakkop.services.hannibal import HannibalGameService

LOGGER = logging.getLogger(__file__)


class GameType(DjangoObjectType):
    class Meta:
        model = Game
        convert_choices_to_enum = False

    creator = graphene.Field(UserType)
    rounds = graphene.List(RoundType)

    def resolve_rounds(self, info, **kwargs):
        return self.rounds.all()


class CreateGame(graphene.Mutation):
    class Arguments:
        creator_id = graphene.ID(required=True)
        game_type = graphene.String(required=True)
        players = graphene.List(PlayerInput)

    game = graphene.Field(GameType)

    def mutate(self, info, creator_id, game_type, players):
        with atomic():
            game = Game.objects.create(creator_id=creator_id, game_type=game_type)
            service = None

            if game_type == constants.HANNIBAL:
                service = HannibalGameService()

            service.generate_players(game, players)
            service.generate_rounds(game)

            return CreateGame(game=game)


class Mutations:
    create_game = CreateGame.Field()
