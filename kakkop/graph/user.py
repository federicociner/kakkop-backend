from graphene_django import DjangoObjectType

from users.models import BaseUser as User


class UserType(DjangoObjectType):
    class Meta:
        model = User
