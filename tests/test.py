from pycool import main
import unittest
import sys
from unittest import mock


class WidgetTestCase(unittest.TestCase):

    def test_first(self):
        print(sys.version_info)
        self.assertTrue(main.main())

if __name__ == '__main__':
    unittest.main()
