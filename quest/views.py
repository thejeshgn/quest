from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,Http404
import json,csv,re
from tracking.utils import get_ip_address
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.template import RequestContext
import logging,requests
from django.contrib import messages
from django.conf import settings
import urllib
from django.views.decorators.csrf import csrf_exempt
import md5
import requests
from .models import *

logger = logging.getLogger(__name__)
HEADER_FORM_URLENCODED = {'content-type':'application/x-www-form-urlencoded'}


def home(request):
    return render_to_response('home.html',{'request':request}, context_instance = RequestContext(request))

def pingHelp(request):
    return render_to_response('markdown.html',{'request':request}, context_instance = RequestContext(request))



def ping(request):
    catalog_url = request.GET.get('catalog', '')
    if catalog_url == "":
        return HttpResponse('Ping error 0: Please provide an url to catalog.json as catalog parameter.')
    url_for_hash = catalog_url
    if catalog_url.startswith("https://"):
        url_for_hash = catalog_url[8:]
    elif catalog_url.startswith("http://"):
        url_for_hash = catalog_url[7:]

    hash_key    = md5.new(url_for_hash).hexdigest()
    client_ip   = request.META['REMOTE_ADDR']
    user_agent  = request.META['HTTP_USER_AGENT']
    content     = ""
    json_content =""
    print catalog_url
    r = requests.get(catalog_url)
    print r
    if r.status_code == 200:
        try:
            json_content = json.loads(r.content)
        except:
            return HttpResponse('Ping error 2: Catalog content is not json')    
    else:
        return HttpResponse('Ping error 1: Catalog URL not available')



    pinglog = PingLog(hash_key=hash_key,ip_address=client_ip,user_agent=user_agent, content=content, url=catalog_url)
    pinglog.save()

    return HttpResponse('All OK')

def schema(request, version):
    return HttpResponse('All OK. Version='+str(version))
