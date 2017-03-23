from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from django.utils.six.moves.urllib.parse import urlsplit

black_list = ('index','fuck','error')

def prep_url(url):
    protocol = get_protocol(url)
    if not protocol:
        url = "http://" + url
    validator = URLValidator()
    try:
        validator(url)
    except ValidationError, e:
        return False,url
    return True,url

def get_protocol(url):
    scheme, netloc, path, query, fragment = urlsplit(url)
    print 'scheme: ' + scheme
    return scheme

def validate_short_url(short_url):
    return (short_url.isalnum() and short_url not in black_list)


