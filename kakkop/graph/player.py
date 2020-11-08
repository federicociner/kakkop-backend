import graphene
from graphene_django import DjangoObjectType

from kakkop.graph.user import UserType
from kakkop.models.player import Player


class PlayerType(DjangoObjectType):
    class Meta:
        model = Player

    user = graphene.Field(UserType)


class PlayerInput(graphene.InputObjectType):
    user_id = graphene.ID(required=True)
    position = graphene.Int(required=True)
    is_first_dealer = graphene.Boolean(required=True)
