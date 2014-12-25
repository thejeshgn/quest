from .models import *
from django.contrib import admin

class PingLogAdmin(admin.ModelAdmin):
    list_display = ('id','hash_key','url','ip_address','user_agent','time')

admin.site.register(PingLog, PingLogAdmin)