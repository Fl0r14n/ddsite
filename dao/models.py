from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from geoposition.fields import GeopositionField
from colorful.fields import RGBColorField
from ckeditor.fields import RichTextField


def to_string(self):
    d = vars(self)
    result = '{'
    for k in sorted(d.keys()):
        if not k.startswith('_'):
            result += '({} : {}), '.format(k, d[k])
    return result + '}\n'


class Image(models.Model):
    image = models.ImageField(upload_to='images')

    class Meta:
        db_table = 'images'

    def __str__(self):
        return self.image.path


class Country(models.Model):
    iso = models.CharField(primary_key=True, max_length=2, help_text='Country 2 letter ISO identifier')
    name = models.CharField(default='', blank=True, max_length=64, help_text='County name')
    flag = models.ImageField(blank=True, help_text='Country flag icon image')

    class Meta:
        db_table = 'countries'
        ordering = ['iso']
        verbose_name_plural = 'Countries'

    def __str__(self):
        return '{} ({})'.format(self.name, self.iso)


class Place(models.Model):
    name = models.CharField(max_length=64, help_text='Place label')
    coordinates = GeopositionField(blank=True, help_text='Place location on the map')
    country = models.ForeignKey(Country, null=True, blank=True, help_text='Country where this place is located')
    city = models.CharField(default='', blank=True, max_length=128, help_text='City where this place is located')
    address = models.CharField(default='', blank=True, max_length=128, help_text='Address')
    postal_code = models.CharField(default='', blank=True, max_length=10, help_text='Postal Code')
    phone = PhoneNumberField(default='', blank=True, help_text='Contact phone number')
    fax = PhoneNumberField(default='', blank=True, help_text='Contact fax number')
    email = models.EmailField(default='', blank=True, help_text='Contact email if any')
    image = models.ImageField(blank=True, help_text='Sample image of that place')

    class Meta:
        db_table = 'places'
        ordering = ['city', 'address']

    def __str__(self):
        return '{}: {} {} {} {}'.format(self.name, self.address, self.postal_code, self.city, self.country)


class Contact(Place):
    class Meta:
        db_table = 'contact'


class Article(models.Model):
    title = models.CharField(max_length=64, help_text='Article title')
    subtitle = models.CharField(default='', blank=True, max_length=64, help_text='Article subtitle')
    description = RichTextField(default='', blank=True, help_text='Article content')
    place = models.ForeignKey(Place, null=True, blank=True, help_text='Assign a place to the article if any')
    image = models.ImageField(null=True, blank=True, help_text='Main article image')
    images = models.ManyToManyField(Image, blank=True, help_text='Collection of images for the article')
    link = models.URLField(default='', blank=True, help_text='External reference for the article')
    style = models.TextField(default='', blank=True, help_text='Some custom css style for the article if any')

    class Meta:
        db_table = 'articles'
        ordering = ['title']

    def __str__(self):
        return ''.format(self.title)


class Job(Article):
    class Meta:
        db_table = 'jobs'


class Event(Article):
    class Meta:
        db_table = 'events'


class Expertise(Article):
    main_item = models.BooleanField(default=False,
                                    help_text='Main Item has greater importance and is rendered differently')

    class Meta:
        db_table = 'expertise'


class Client(Article):
    case_study_link = models.URLField(default='', blank=True, help_text='External/Internal link for more details')

    class Meta:
        db_table = 'clients'


class BusinessDomain(Article):
    percentage = models.IntegerField(default='', blank=True,
                                     help_text='Percent of business value this particular domain has')
    color = RGBColorField(default='', blank=True, max_length=16,
                          help_text='Representative color for this particular business domain')

    class Meta:
        db_table = 'business_domains'


class Blog(Article):
    class Meta:
        db_table = 'blogs'
