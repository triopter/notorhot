# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Candidate.slug'
        db.add_column(u'notorhot_candidate', 'slug',
                      self.gf('autoslug.fields.AutoSlugField')(default='', unique_with=(), max_length=50, populate_from='name', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Candidate.slug'
        db.delete_column(u'notorhot_candidate', 'slug')


    models = {
        u'notorhot.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'challenges': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pic': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'", 'blank': 'True'}),
            'votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'wins': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'})
        },
        u'notorhot.competition': {
            'Meta': {'object_name': 'Competition'},
            'date_presented': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_voted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'left': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comparisons_left'", 'to': u"orm['notorhot.Candidate']"}),
            'right': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comparisons_right'", 'to': u"orm['notorhot.Candidate']"}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'comparisons_won'", 'null': 'True', 'to': u"orm['notorhot.Candidate']"}),
            'winning_side': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['notorhot']