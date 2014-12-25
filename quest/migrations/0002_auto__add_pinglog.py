# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PingLog'
        db.create_table(u'quest_pinglog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hash_key', self.gf('django.db.models.fields.TextField')(null=True)),
            ('ip_address', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('user_agent', self.gf('django.db.models.fields.TextField')(null=True)),
            ('content', self.gf('jsonfield.fields.JSONField')(null=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'quest', ['PingLog'])


    def backwards(self, orm):
        # Deleting model 'PingLog'
        db.delete_table(u'quest_pinglog')


    models = {
        u'quest.pinglog': {
            'Meta': {'object_name': 'PingLog'},
            'content': ('jsonfield.fields.JSONField', [], {'null': 'True'}),
            'hash_key': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user_agent': ('django.db.models.fields.TextField', [], {'null': 'True'})
        }
    }

    complete_apps = ['quest']