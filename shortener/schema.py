import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q
from graphql import GraphQLError
from .models import URL
from applications.models import Application


class URLType(DjangoObjectType):
    class Meta:
        model = URL


class Query(graphene.ObjectType):
    urls = graphene.List(URLType, url=graphene.String(),
                         application_token=graphene.String())

    def resolve_urls(self, info, url=None, application_token=None,  **kwargs):

        try:
            application = Application.objects.get(token=application_token)
        except Exception:
            raise GraphQLError('Invalid Application Token')

        queryset = URL.objects.filter(application=application)

        # if application:
        #     if url:
        #         _filter = Q(full_url__icontains=url)
        #         queryset = queryset.filter(_filter)

        return queryset
