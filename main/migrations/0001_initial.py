# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserAgent'
        db.create_table(u'main_useragent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'main', ['UserAgent'])

        # Adding model 'UserSession'
        db.create_table(u'main_usersession', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('ip_address', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('user_agent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.UserAgent'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['UserSession'])

        # Adding model 'UserSessionVisitedUrls'
        db.create_table(u'main_usersessionvisitedurls', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.UserSession'])),
        ))
        db.send_create_signal(u'main', ['UserSessionVisitedUrls'])

        # Adding model 'Review'
        db.create_table(u'main_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1, db_index=True)),
            ('result', self.gf('django.db.models.fields.NullBooleanField')(default=None, null=True, blank=True)),
            ('result_reasoning', self.gf('django.db.models.fields.TextField')(null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Review'])

        # Adding model 'MusicGenre'
        db.create_table(u'main_musicgenre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('reviewed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.UserSession'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['MusicGenre'])

        # Adding model 'MusicProgram'
        db.create_table(u'main_musicprogram', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('reviewed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.UserSession'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['MusicProgram'])

        # Adding model 'MusicPlugins'
        db.create_table(u'main_musicplugins', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('software', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.MusicProgram'])),
            ('reviewed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.UserSession'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['MusicPlugins'])

        # Adding model 'MusicBanks'
        db.create_table(u'main_musicbanks', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('plugin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.MusicPlugins'])),
            ('reviewed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.UserSession'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['MusicBanks'])

        # Adding model 'UploadedFolderTmpFile'
        db.create_table(u'main_uploadedfoldertmpfile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('directory_identifier', self.gf('django.db.models.fields.CharField')(max_length=36, db_index=True)),
            ('storage_filename', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36)),
            ('original_filename', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('file_size_in_bytes', self.gf('django.db.models.fields.BigIntegerField')()),
            ('mime_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.UserSession'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['UploadedFolderTmpFile'])

        # Adding model 'ProjectFileCategory'
        db.create_table(u'main_projectfilecategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['ProjectFileCategory'])

        # Adding model 'ProjectFile'
        db.create_table(u'main_projectfile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alive', self.gf('edm.models.LiveField')(default=True, null=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.ProjectFileCategory'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], db_column='created_by')),
        ))
        db.send_create_signal(u'main', ['ProjectFile'])

        # Adding model 'ProjectFileVersion'
        db.create_table(u'main_projectfileversion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_file', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.ProjectFile'])),
            ('review', self.gf('django.db.models.fields.related.OneToOneField')(related_name='review_of', unique=True, to=orm['main.Review'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('bpm', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.UserSession'])),
            ('genre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.MusicGenre'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['ProjectFileVersion'])

        # Adding M2M table for field compatible_programs on 'ProjectFileVersion'
        m2m_table_name = db.shorten_name(u'main_projectfileversion_compatible_programs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectfileversion', models.ForeignKey(orm[u'main.projectfileversion'], null=False)),
            ('musicprogram', models.ForeignKey(orm[u'main.musicprogram'], null=False))
        ))
        db.create_unique(m2m_table_name, ['projectfileversion_id', 'musicprogram_id'])

        # Adding M2M table for field compatible_plugins on 'ProjectFileVersion'
        m2m_table_name = db.shorten_name(u'main_projectfileversion_compatible_plugins')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectfileversion', models.ForeignKey(orm[u'main.projectfileversion'], null=False)),
            ('musicplugins', models.ForeignKey(orm[u'main.musicplugins'], null=False))
        ))
        db.create_unique(m2m_table_name, ['projectfileversion_id', 'musicplugins_id'])

        # Adding M2M table for field compatible_banks on 'ProjectFileVersion'
        m2m_table_name = db.shorten_name(u'main_projectfileversion_compatible_banks')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectfileversion', models.ForeignKey(orm[u'main.projectfileversion'], null=False)),
            ('musicbanks', models.ForeignKey(orm[u'main.musicbanks'], null=False))
        ))
        db.create_unique(m2m_table_name, ['projectfileversion_id', 'musicbanks_id'])

        # Adding model 'UploadedFile'
        db.create_table(u'main_uploadedfile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.PositiveSmallIntegerField')(db_index=True)),
            ('storage_filename', self.gf('django.db.models.fields.CharField')(unique=True, max_length=36)),
            ('original_filename', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('file_size_in_bytes', self.gf('django.db.models.fields.BigIntegerField')()),
            ('mime_type', self.gf('django.db.models.fields.CharField')(default=None, max_length=255)),
            ('meta_data', self.gf('jsonfield.fields.JSONField')()),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.UserSession'])),
            ('uploader', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], db_column='created_by')),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('project_file_version', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.ProjectFileVersion'])),
        ))
        db.send_create_signal(u'main', ['UploadedFile'])

        # Adding model 'Purchase'
        db.create_table(u'main_purchase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('project_file_version', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.ProjectFileVersion'])),
            ('state', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1)),
            ('session', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.UserSession'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Purchase'])


    def backwards(self, orm):
        # Deleting model 'UserAgent'
        db.delete_table(u'main_useragent')

        # Deleting model 'UserSession'
        db.delete_table(u'main_usersession')

        # Deleting model 'UserSessionVisitedUrls'
        db.delete_table(u'main_usersessionvisitedurls')

        # Deleting model 'Review'
        db.delete_table(u'main_review')

        # Deleting model 'MusicGenre'
        db.delete_table(u'main_musicgenre')

        # Deleting model 'MusicProgram'
        db.delete_table(u'main_musicprogram')

        # Deleting model 'MusicPlugins'
        db.delete_table(u'main_musicplugins')

        # Deleting model 'MusicBanks'
        db.delete_table(u'main_musicbanks')

        # Deleting model 'UploadedFolderTmpFile'
        db.delete_table(u'main_uploadedfoldertmpfile')

        # Deleting model 'ProjectFileCategory'
        db.delete_table(u'main_projectfilecategory')

        # Deleting model 'ProjectFile'
        db.delete_table(u'main_projectfile')

        # Deleting model 'ProjectFileVersion'
        db.delete_table(u'main_projectfileversion')

        # Removing M2M table for field compatible_programs on 'ProjectFileVersion'
        db.delete_table(db.shorten_name(u'main_projectfileversion_compatible_programs'))

        # Removing M2M table for field compatible_plugins on 'ProjectFileVersion'
        db.delete_table(db.shorten_name(u'main_projectfileversion_compatible_plugins'))

        # Removing M2M table for field compatible_banks on 'ProjectFileVersion'
        db.delete_table(db.shorten_name(u'main_projectfileversion_compatible_banks'))

        # Deleting model 'UploadedFile'
        db.delete_table(u'main_uploadedfile')

        # Deleting model 'Purchase'
        db.delete_table(u'main_purchase')


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
        u'main.musicbanks': {
            'Meta': {'object_name': 'MusicBanks'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'plugin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.MusicPlugins']"}),
            'reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.UserSession']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'main.musicgenre': {
            'Meta': {'object_name': 'MusicGenre'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.UserSession']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'main.musicplugins': {
            'Meta': {'object_name': 'MusicPlugins'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.UserSession']"}),
            'software': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.MusicProgram']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'main.musicprogram': {
            'Meta': {'object_name': 'MusicProgram'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'reviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.UserSession']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'main.projectfile': {
            'Meta': {'object_name': 'ProjectFile'},
            'alive': ('edm.models.LiveField', [], {'default': 'True', 'null': 'True'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'db_column': "'created_by'"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.ProjectFileCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'main.projectfilecategory': {
            'Meta': {'object_name': 'ProjectFileCategory'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'main.projectfileversion': {
            'Meta': {'object_name': 'ProjectFileVersion'},
            'bpm': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'compatible_banks': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.MusicBanks']", 'symmetrical': 'False'}),
            'compatible_plugins': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.MusicPlugins']", 'symmetrical': 'False'}),
            'compatible_programs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['main.MusicProgram']", 'symmetrical': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.MusicGenre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'project_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.ProjectFile']"}),
            'review': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'review_of'", 'unique': 'True', 'to': u"orm['main.Review']"}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.UserSession']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'main.purchase': {
            'Meta': {'object_name': 'Purchase'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_file_version': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.ProjectFileVersion']"}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.UserSession']"}),
            'state': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'main.review': {
            'Meta': {'object_name': 'Review'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'result_reasoning': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'state': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'main.uploadedfile': {
            'Meta': {'object_name': 'UploadedFile'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file_size_in_bytes': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_data': ('jsonfield.fields.JSONField', [], {}),
            'mime_type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'project_file_version': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.ProjectFileVersion']"}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.UserSession']"}),
            'storage_filename': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36'}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {'db_index': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uploader': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'db_column': "'created_by'"})
        },
        u'main.uploadedfoldertmpfile': {
            'Meta': {'object_name': 'UploadedFolderTmpFile'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'directory_identifier': ('django.db.models.fields.CharField', [], {'max_length': '36', 'db_index': 'True'}),
            'file_size_in_bytes': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mime_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.UserSession']"}),
            'storage_filename': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '36'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'main.useragent': {
            'Meta': {'object_name': 'UserAgent'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        u'main.usersession': {
            'Meta': {'object_name': 'UserSession'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_agent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.UserAgent']"})
        },
        u'main.usersessionvisitedurls': {
            'Meta': {'object_name': 'UserSessionVisitedUrls'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.UserSession']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['main']