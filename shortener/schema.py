import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q
from .models import URL


class URLType(DjangoObjectType):
    class Meta:
        model = URL


class Query(graphene.ObjectType):
    urls = graphene.List(URLType , url = graphene.String() , first=graphene.Int(), skip=graphene.Int())

    def resolve_urls(self, info, url = None ,**kwargs):
        queryset = URL.objects.all()

        if url:
             _filter = Q(full_url__icontains=url)
             queryset = queryset.filter(_filter)
        if first:
            queryset = queryset[:first]

        if skip:
            queryset = queryset[skip:]
        return URL.objects.all()