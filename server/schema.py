import graphene
from graphene_django import DjangoObjectType

from server.stores.models import Category, Stores

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")

class StoresType(DjangoObjectType):
    class Meta:
        model = Stores
        fields = ("id", "name")

class Query(graphene.ObjectType):
    all_stores = graphene.List(StoresType)

    def resolve_all_stores(root, info):
        # TODO: Filter out what we need, different logic goes in here
        return Stores.objects.all()

    # TODO: Add mutations 
    
schema = graphene.Schema(query=Query)