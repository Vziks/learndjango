# -*- coding: utf-8 -*-

import os

from urlparse import urlparse
from django import template
from django.template.defaultfilters import stringfilter
from app import settings

register = template.Library()

def _absolute_url(url):
    if url.startswith('http://') or url.startswith('https://'):
        return url
    domain = Site.objects.get_current().domain
    return 'http://%s%s' % (domain, url)

@register.simple_tag
def media(filename, flags=''):
    flags = set(f.strip() for f in flags.split(','))
    # url = urlparse.urljoin(settings.MEDIA_URL, filename)
    url = os.path.join(settings.MEDIA_URL, filename)
    if 'absolute' in flags:
        url = _absolute_url(url)
    if (filename.endswith('.css') or filename.endswith('.js')) and 'no-timestamp' not in flags or \
                    'timestamp' in flags:
        fullname = os.path.join(settings.MEDIA_ROOT, filename)
        if os.path.exists(fullname):
            url += '?%d' % os.path.getmtime(fullname)
    return url