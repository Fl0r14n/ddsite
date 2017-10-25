from tastypie.resources import ModelResource
from tastypie import fields
from dao.models import *
from tastypie.paginator import Paginator
from tastypie.authorization import ReadOnlyAuthorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS

authorization = ReadOnlyAuthorization()

class BlogResource(ModelResource):
    class Meta:
        queryset = Blog.objects.all()
        resource_name = 'blog'
        paginator_class = Paginator
        authorization = authorization


class BusinessDomainResource(ModelResource):
    class Meta:
        queryset = BusinessDomain.objects.all()
        resource_name = 'domain'
        paginator_class = Paginator
        authorization = authorization


class ClientResource(ModelResource):
    class Meta:
        queryset = Client.objects.all()
        resource_name = 'client'
        paginator_class = Paginator
        authorization = authorization


class ExpertiseResource(ModelResource):
    class Meta:
        queryset = Expertise.objects.all()
        resource_name = 'expertise'
        paginator_class = Paginator
        authorization = authorization


class EventResource(ModelResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        paginator_class = Paginator
        authorization = authorization


class PositionResource(ModelResource):
    class Meta:
        queryset = Job.objects.all()
        resource_name = 'position'
        paginator_class = Paginator
        authorization = authorization


class ContactResource(ModelResource):
    class Meta:
        queryset = Contact.objects.all()
        resource_name = 'contact'
        paginator_class = Paginator
        authorization = authorization
