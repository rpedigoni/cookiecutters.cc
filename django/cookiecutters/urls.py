# coding: utf-8
from django.conf.urls import patterns, include, url
from projects.views import LanguageListView

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', LanguageListView.as_view()),
    # url(r'^admin/', include(admin.site.urls)),
)
