import graphene
from graphene_django import DjangoObjectType

from server.businesses.models import Business
class BusinessType(DjangoObjectType):
    # TODO: Add the different fields for businesses here! 
    class Meta:
        model = Business
        # TODO: Or we can just choose the fields to return here

class Query(graphene.ObjectType):
    all_stores = graphene.List(StoresType)
    store_with_tags_city = graphene.List(StoresType, tags=graphene.String(), city=graphene.String())
    # store_near_city = graphene.List(StoresType)

    def resolve_all_stores(root, info):
        return Business.objects.all()

    def resolve_store_with_tags_city(root, info, tags, city):
        if tags is None and city is None: 
            return None 
        elif tags is None:
            return Business.objects.filter(tags=tags)
        elif city is None: 
            return Business.objects.filter(city=city)
        else:  
            return Business.objects.filter(tags=tags, city=city) 
    
schema = graphene.Schema(query=Query)