import graphene
import shortener.schema
import shortener.mutation


class Query(shortener.schema.Query, graphene.ObjectType):
    pass


class Mutation(shortener.mutation.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
