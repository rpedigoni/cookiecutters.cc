# coding: utf-8
from django.test.testcases import TestCase
from factories import LanguageFactory, TemplateFactory


class TemplateTestCase(TestCase):
    def test_list(self):
        for name in ('Python', 'C++', 'Java'):
            language = LanguageFactory.create(name=name)
            [TemplateFactory.create(language=language) for t in range(3)]


        response = self.client.get('/')
        print response.content
        self.assertEqual(response.status_code, 200)
