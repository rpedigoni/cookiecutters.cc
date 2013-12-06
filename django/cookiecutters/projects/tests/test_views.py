# coding: utf-8
from django.test.testcases import TestCase
from factories import LanguageFactory, ProjectFactory


class ProjectTestCase(TestCase):
    def test_list(self):
        for name in ('Python', 'C++', 'Java'):
            language = LanguageFactory.create(name=name)
            [ProjectFactory.create(language=language) for t in range(3)]

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
