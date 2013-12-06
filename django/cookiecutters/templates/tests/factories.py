# coding: utf-8
import factory
from templates.models import Language, Template


class LanguageFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = Language

    name = u'Python'


class TemplateFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = Template

    language = factory.SubFactory(LanguageFactory)
    name = u'cookiecutter-django-project'
    author = u'Renato Pedigoni'
    repository_url = u'https://github.com/rpedigoni/cookiecutter-django-project'
