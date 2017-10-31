from tastypie.resources import ModelResource
from tastypie import fields
from dao.models import *
from tastypie.paginator import Paginator
from tastypie.authorization import ReadOnlyAuthorization
from api.serializers import CamelCaseJSONSerializer

authorization = ReadOnlyAuthorization()
serializer = CamelCaseJSONSerializer()


class ImageResource(ModelResource):
    class Meta:
        queryset = Image.objects.all()
        resource_name = 'image'
        paginator_class = Paginator
        authorization = authorization
        serializer = serializer


class CountryResource(ModelResource):
    class Meta:
        queryset = Country.objects.all()
        resource_name = 'country'
        paginator_class = Paginator
        authorization = authorization
        serializer = serializer


class PlaceResource(ModelResource):
    country = fields.ToOneField(CountryResource, 'country', null=True, blank=True, full=True)

    class Meta:
        queryset = Place.objects.all()
        resource_name = 'place'
        paginator_class = Paginator
        authorization = authorization
        serializer = serializer

    def dehydrate_coordinates(self, bundle):
        return {
            'latitude': bundle.obj.coordinates.y,
            'longitude': bundle.obj.coordinates.x
        }


class ArticleResource(ModelResource):
    images = fields.ToManyField(ImageResource, 'images', null=True, blank=True, full=True)

    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'
        paginator_class = Paginator
        authorization = authorization
        serializer = serializer


class BlogResource(ArticleResource):
    class Meta:
        queryset = Blog.objects.all()
        resource_name = 'blog'
        paginator_class = Paginator
        authorization = authorization
        serializer = serializer


class BusinessDomainResource(ArticleResource):
    class Meta:
        queryset = BusinessDomain.objects.all()
        resource_name = 'domain'
        paginator_class = Paginator
        authorization = authorization
        serializer = serializer


class ClientResource(ArticleResource):
    class Meta:
        queryset = Client.objects.all()
        resource_name = 'client'
        paginator_class = Paginator
        authorization = authorization
        serializer = serializer


class ExpertiseResource(ArticleResource):
    class Meta:
        queryset = Expertise.objects.all()
        resource_name = 'expertise'
        paginator_class = Paginator
        authorization = authorization
        serializer = serializer


class EventResource(ArticleResource):
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        paginator_class = Paginator
        authorization = authorization
        serializer = serializer


class PositionResource(ArticleResource):
    class Meta:
        queryset = Job.objects.all()
        resource_name = 'position'
        paginator_class = Paginator
        authorization = authorization
        serializer = serializer


class ContactResource(PlaceResource):
    class Meta:
        queryset = Contact.objects.all()
        resource_name = 'contact'
        paginator_class = Paginator
        authorization = authorization
        serializer = serializer
