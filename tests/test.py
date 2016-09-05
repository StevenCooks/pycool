from pycool import main
import unittest


class WidgetTestCase(unittest.TestCase):

    def test_first(self):
        self.assertTrue(main.main())

if __name__ == '__main__':
    unittest.main()
