# coding: utf-8
from django.test.testcases import TestCase
from factories import LanguageFactory, ProjectFactory


class LanguageTestCase(TestCase):
    def test_model_unicode(self):
        language = LanguageFactory.create()

        self.assertEqual(unicode(language), language.name)


class ProjectTestCase(TestCase):
    def test_model_unicode(self):
        project = ProjectFactory.create()

        self.assertEqual(unicode(project), project.name)
