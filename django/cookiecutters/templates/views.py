# coding: utf-8
from django.views.generic import ListView
from models import Language


class LanguageListView(ListView):
    queryset = Language.objects.all()
    template_name = 'templates/template_list.html'
