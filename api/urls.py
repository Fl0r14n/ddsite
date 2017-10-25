from django.conf.urls import include, url
from tastypie.api import Api

from api.resources import *

api_version = 'v1'

v1_api = Api(api_name=api_version)
v1_api.register(BlogResource())
v1_api.register(BusinessDomainResource())
v1_api.register(ClientResource())
v1_api.register(ExpertiseResource())
v1_api.register(EventResource())
v1_api.register(PositionResource())
v1_api.register(ContactResource())

urlpatterns = [
    url(r'^api/', include(v1_api.urls)),
]
