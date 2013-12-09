# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Language'
        db.create_table(u'projects_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'projects', ['Language'])

        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Language'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('repository_url', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'projects', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Language'
        db.delete_table(u'projects_language')

        # Deleting model 'Project'
        db.delete_table(u'projects_project')


    models = {
        u'projects.language': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Language'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'projects.project': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Project'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projects.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'repository_url': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['projects']