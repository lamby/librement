import random
import itertools

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

def invent_username(first_name, last_name):
    counter = itertools.count(random.randrange(1000000))

    base = slugify(u'%s%s' % (first_name, last_name))

    username = base or 'user'

    while User.objects.filter(username=username).exists():
        # We must ensure that our username suggestions are under 30
        # characters or we'll simply fail later when we try and create a
        # User (hence the [:30]), but we also need space for the variable
        # suffix (hence the [:25]) or we run the risk of entering into
        # infinite loop trying the same combination again and again.
        username = '%s%d' % (base[:25], counter.next())
        username = username[:30]

    return username
