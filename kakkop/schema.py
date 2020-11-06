import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello world!")


schema = graphene.Schema(query=Query)
