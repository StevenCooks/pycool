###############################################################################
# test_string.py
# How to test: make sure you are using Python 3
#   pycool $> pyenv ./bin/activate
#
#   pycool $> make
# Or,
#   pycool $> make run
# Or,
#   coverage run -m unittest discover tests
###############################################################################
from unittest import TestCase

from pycool.py import string


class StringTestCase(TestCase):

    def test_fill_template(self):
        name = "my name"
        fill1 = string.fill_template(name)
        fill2 = string.fill_template_dict(name)
        fill3 = string.fill_template_named(name)
        self.assertEqual(fill1, fill2)
        self.assertEqual(fill3, fill2)
