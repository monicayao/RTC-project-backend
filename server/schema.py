import graphene
from graphene_django import DjangoObjectType

from server.business.models import Business
class BusinessType(DjangoObjectType):
    # TODO: Add the different fields for businesses here! 
    class Meta:
        model = Business
        # TODO: Or we can just choose the fields to return here

class Query(graphene.ObjectType):
    all_business = graphene.List(BusinessType)
    business_with_tags_city = graphene.List(BusinessType, tags=graphene.String(), city=graphene.String())

    def resolve_all_business(root, info):
        return Business.objects.all()

    def resolve_business_with_tags_city(root, info, tags, city):
        if tags is None and city is None: 
            return None 
        elif tags is None:
            return Business.objects.filter(tags=tags)
        elif city is None: 
            return Business.objects.filter(city=city)
        else:  
            return Business.objects.filter(tags=tags, city=city) 
    
schema = graphene.Schema(query=Query)