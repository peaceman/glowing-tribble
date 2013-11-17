# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UploadedFolderTmpFile'
        db.create_table(u'edmupload_uploadedfoldertmpfile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('directory_identifier', self.gf('django.db.models.fields.CharField')(max_length=36, db_index=True)),
            ('storage_filename', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36)),
            ('original_filename', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('file_size_in_bytes', self.gf('django.db.models.fields.BigIntegerField')()),
            ('mime_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['edmuser.UserSession'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'edmupload', ['UploadedFolderTmpFile'])

        # Adding model 'UploadedFile'
        db.create_table(u'edmupload_uploadedfile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.PositiveSmallIntegerField')(db_index=True)),
            ('storage_filename', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36)),
            ('original_filename', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('file_size_in_bytes', self.gf('django.db.models.fields.BigIntegerField')()),
            ('mime_type', self.gf('django.db.models.fields.CharField')(default=None, max_length=255)),
            ('meta_data', self.gf('jsonfield.fields.JSONField')()),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['edmuser.UserSession'])),
            ('uploader', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], db_column='created_by')),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('project_file_version', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['edmproject.ProjectFileVersion'])),
        ))
        db.send_create_signal(u'edmupload', ['UploadedFile'])


    def backwards(self, orm):
        # Deleting model 'UploadedFolderTmpFile'
        db.delete_table(u'edmupload_uploadedfoldertmpfile')

        # Deleting model 'UploadedFile'
        db.delete_table(u'edmupload_uploadedfile')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'edmmusic.musicbanks': {
            'Meta': {'object_name': 'MusicBanks'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'plugin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edmmusic.MusicPlugins']"}),
            'reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edmuser.UserSession']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'edmmusic.musicgenre': {
            'Meta': {'object_name': 'MusicGenre'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edmuser.UserSession']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'edmmusic.musicplugins': {
            'Meta': {'object_name': 'MusicPlugins'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edmuser.UserSession']"}),
            'software': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edmmusic.MusicProgram']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'edmmusic.musicprogram': {
            'Meta': {'object_name': 'MusicProgram'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edmuser.UserSession']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'edmproject.projectfile': {
            'Meta': {'object_name': 'ProjectFile'},
            'alive': ('edm.models.LiveField', [], {'default': 'True', 'null': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'db_column': "'created_by'"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edmproject.ProjectFileCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'edmproject.projectfilecategory': {
            'Meta': {'object_name': 'ProjectFileCategory'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'edmproject.projectfileversion': {
            'Meta': {'object_name': 'ProjectFileVersion'},
            'bpm': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'compatible_banks': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['edmmusic.MusicBanks']", 'symmetrical': 'False'}),
            'compatible_plugins': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['edmmusic.MusicPlugins']", 'symmetrical': 'False'}),
            'compatible_programs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['edmmusic.MusicProgram']", 'symmetrical': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edmmusic.MusicGenre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'project_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edmproject.ProjectFile']"}),
            'review': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'review_of'", 'unique': 'True', 'to': u"orm['edmreview.Review']"}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edmuser.UserSession']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'edmreview.review': {
            'Meta': {'object_name': 'Review'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'result_reasoning': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'edmupload.uploadedfile': {
            'Meta': {'object_name': 'UploadedFile'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file_size_in_bytes': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_data': ('jsonfield.fields.JSONField', [], {}),
            'mime_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'project_file_version': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edmproject.ProjectFileVersion']"}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edmuser.UserSession']"}),
            'storage_filename': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36'}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uploader': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'db_column': "'created_by'"})
        },
        u'edmupload.uploadedfoldertmpfile': {
            'Meta': {'object_name': 'UploadedFolderTmpFile'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'directory_identifier': ('django.db.models.fields.CharField', [], {'max_length': '36', 'db_index': 'True'}),
            'file_size_in_bytes': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mime_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edmuser.UserSession']"}),
            'storage_filename': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'edmuser.useragent': {
            'Meta': {'object_name': 'UserAgent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        u'edmuser.usersession': {
            'Meta': {'object_name': 'UserSession'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_agent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['edmuser.UserAgent']"})
        }
    }

    complete_apps = ['edmupload']