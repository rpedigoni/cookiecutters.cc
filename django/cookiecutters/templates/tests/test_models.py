# coding: utf-8
from django.test.testcases import TestCase
from factories import LanguageFactory, TemplateFactory


class LanguageTestCase(TestCase):
    def test_model_unicode(self):
        language = LanguageFactory.create()

        self.assertEqual(unicode(language), language.name)


class TemplateTestCase(TestCase):
    def test_model_unicode(self):
        template = TemplateFactory.create()

        self.assertEqual(unicode(template), template.name)
