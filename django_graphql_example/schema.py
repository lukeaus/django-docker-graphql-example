import graphene
from ingredients import schema as ingredients_schema


class Query(
        ingredients_schema.Query,
        graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
