from unittest import TestCase
from unittest.mock import MagicMock

from pycool import main


class WidgetTestCase(TestCase):

    def test_first(self):
        self.assertTrue(main.main())


if __name__ == '__main__':
    unittest.main()
