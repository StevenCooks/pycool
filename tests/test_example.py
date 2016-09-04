############################################################
# test_example.py
#
# - Mock an item where it is used, not where it came from.
#
############################################################
from unittest import TestCase
from unittest.mock import patch

from pycool.example.util import rm


class ExampleTestCase(TestCase):

    @patch('pycool.example.util.os.path')
    @patch('pycool.example.util.os')
    def test_util_rm(self, mock_os, mock_path):
        """ Note: we are patching `os` module in `pycool.example.util`
        not, `os` module from python builtin."""

        # patch os.path module and specify return_value of inside methods
        mock_path.isfile.return_value = False
        rm("haha")
        self.assertFalse(mock_os.remove.called)

        mock_path.isfile.return_value = True
        rm("haha")
        mock_os.remove.assert_called_with("haha")


