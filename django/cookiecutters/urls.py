# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from projects.views import LanguageListView


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', LanguageListView.as_view()),
)
