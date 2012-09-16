from django.db import models

from django_enumfield import EnumField

from librement.utils.user_data import PerUserData

from .enums import AccountEnum, CountryEnum

class Profile(PerUserData('profile')):
    account_type = EnumField(AccountEnum)

    organisation = models.CharField(max_length=100, blank=True)

    address_1 = models.CharField(max_length=150, blank=True)
    address_2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=100, blank=True)

    country = EnumField(CountryEnum)

class Email(models.Model):
    user = models.ForeignKey('auth.User', related_name='emails')

    email = models.EmailField(unique=True)

    def __unicode__(self):
        return u"%s" % self.email
