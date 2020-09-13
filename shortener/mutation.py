import graphene
from graphene_django import DjangoObjectType
from .schema import URLType
from .models import URL
from graphql import GraphQLError
from applications.models import Application

class CreateURL(graphene.Mutation):
    url = graphene.Field(URLType)
    class Arguments:
        full_url = graphene.String(required=True)
        application_token = graphene.String(required=True)

    def mutate(self, info, full_url , application_token):
        found = False
        try:
            application = Application.objects.get(token = application_token)
            found = True
        except Exception:
            raise GraphQLError('Invalid Application Token')
        url = URL(full_url=full_url , application = application)
        url.save()
        return CreateURL(url=url)

class Mutation(graphene.ObjectType):
    create_url = CreateURL.Field()