from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
import urlparse
from jsonfield import JSONField
from django.core import serializers
from collections import OrderedDict
from django.contrib.auth.models import User


    
class PingLog(models.Model):
    # Update to GenericIPAddress in Django 1.4
    hash_key = models.TextField(null=True,editable=False)
    ip_address = models.GenericIPAddressField(editable=False)
    user_agent = models.TextField(null=True, editable=False)
    content = JSONField(null=True,editable=False)
    url = models.CharField(max_length=200,editable=False)
    time = models.DateTimeField(auto_now_add=True,editable=False)
