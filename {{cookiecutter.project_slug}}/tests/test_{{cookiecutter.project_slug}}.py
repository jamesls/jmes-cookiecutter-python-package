import unittest

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}


class Test{{ cookiecutter.project_slug|capitalize }}(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_something(self):
        pass
