# coding: utf-8
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext as _


class Language(models.Model):
    name = models.CharField(_('name'), max_length=32)

    def __unicode__(self):
        return self.name


class Template(models.Model):
    language = models.ForeignKey(Language, verbose_name=_('language'))
    name = models.CharField(_('name'), max_length=64)
    author = models.CharField(_('author'), max_length=64)
    repository_url = models.CharField(_('author'), max_length=64)
    description = models.TextField(_('description'))
    created_at = models.DateTimeField(_('created at'), default=now)

    def __unicode__(self):
        return self.name
