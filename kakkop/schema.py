import graphene

from .graph import game


class TestQuery(graphene.ObjectType):
    hello = graphene.String(default_value="Hello world!")


class Mutation(game.Mutations, graphene.ObjectType):
    pass


class Query(TestQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
