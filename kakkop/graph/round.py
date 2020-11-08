from graphene_django import DjangoObjectType

from kakkop.models.round import Round


class RoundType(DjangoObjectType):
    class Meta:
        model = Round
        convert_choices_to_enum = False
