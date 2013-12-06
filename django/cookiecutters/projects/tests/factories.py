# coding: utf-8
import factory
from projects.models import Language, Project


class LanguageFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = Language

    name = u'Python'


class ProjectFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = Project

    language = factory.SubFactory(LanguageFactory)
    name = u'cookiecutter-django-project'
    author = u'Renato Pedigoni'
    repository_url = u'https://github.com/rpedigoni/cookiecutter-django-project'
