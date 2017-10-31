from django.contrib import admin
from mapwidgets import GooglePointFieldWidget

from dao.models import *


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'iso', 'flag',)
    list_filter = ('iso',)
    search_fields = ('iso', 'name',)
    fieldsets = (
        (None, {
            'fields': ('iso',)
        }),
        ('Details', {
            'fields': ('name', 'flag',)
        })
    )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'address', 'postal_code', 'phone', 'email',)
    list_filter = ('country', 'city')
    search_fields = ('name', 'address', 'city', 'postal_code', 'country', 'phone', 'fax', 'email')
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        ('Address', {
            'fields': ('address', 'city', 'postal_code', 'country',)
        }),
        ('Contact', {
            'fields': ('email', 'phone', 'fax',)
        }),
        ('Other', {
            'fields': ('image', 'coordinates')
        })
    )
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }


@admin.register(Contact)
class ContactAdmin(PlaceAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)
    search_fields = ('image',)


class ArticleInline(admin.TabularInline):
    model = Article.images.through
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'description']
    list_filter = ['title', ]
    search_fields = ['title', 'subtitle', 'description']
    fieldsets = [
        ('Content', {
            'fields': ['title', 'subtitle', 'description']
        }),
        ('Images', {
            'fields': ['image', ]
        }),
        ('Other', {
            'fields': ['link', 'style', 'place']
        })
    ]
    inlines = [ArticleInline, ]


@admin.register(Job)
class JobAdmin(ArticleAdmin):
    fieldsets = [
        ('Content', {
            'fields': ['title', 'subtitle', 'description']
        }),
        ('Other', {
            'fields': ['place']
        })
    ]
    inlines = []


@admin.register(Event)
class EventAdmin(ArticleAdmin):
    fieldsets = [
        ('Content', {
            'fields': ['title', 'description']
        }),
    ]


@admin.register(Expertise)
class ExpertiseAdmin(ArticleAdmin):
    fieldsets = [
        (None, {
            'fields': ['main_item', ]
        }),
        ('Content', {
            'fields': ['title', 'description', ]
        }),
        ('Images', {
            'fields': ['image', ]
        }),
        ('Other', {
            'fields': ['link', 'style', ]
        })
    ]
    inlines = []


@admin.register(Client)
class ClientAdmin(ArticleAdmin):
    list_display = ['title', 'description']
    fieldsets = [
        ('Content', {
            'fields': ['title', 'description']
        }),
        ('Images', {
            'fields': ['image', ]
        }),
        ('Other', {
            'fields': ['link', 'case_study_link']
        })
    ]
    inlines = []


@admin.register(BusinessDomain)
class BusinessDomainAdmin(ArticleAdmin):
    list_display = ['title', 'description']
    fieldsets = [
        ('Content', {
            'fields': ['title', 'description', 'percentage']
        }),
        ('Other', {
            'fields': ['link', 'color']
        })
    ]
    inlines = []


@admin.register(Blog)
class BlogAdmin(ArticleAdmin):
    pass
