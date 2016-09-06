###############################################################################
# test_example.py
#
# - Mock an item where it is used, not where it came from.
#
# 1) ExampleTestCase          : patch builtin module to patch builtin methods
# 2) RemovalServiceTestCase   : patch module function
# 3) UploadServiceTestCase    : patch module's object(instance) method
# 4) UploadServiceMockInstance: create_autospec
#
# Reference:
# [1] https://www.toptal.com/python/an-introduction-to-mocking-in-python
# [2] https://docs.python.org/3/library/unittest.mock.html#autospeccing
#
###############################################################################
from unittest import TestCase
from unittest import mock
from unittest.mock import patch

from pycool.example.util import rm
from pycool.example.util import RemovalService, UploadService


class ExampleTestCase(TestCase):
    """Test module method.
    Patch builtin module to modify behavior of buitlin methods."""

    @patch('pycool.example.util.os.path')
    @patch('pycool.example.util.os')
    def test_util_rm(self, mock_os, mock_path):
        """
        Note:
        1) import: we don't import `os`, `os.path` at this test file, we only
           import module function `rm` from `pycool.example.util`.
        2) @patch: we are patching `os` module in `pycool.example.util`, not
           `os` module from python builtin.
        """
        # specify return_value of inside methods
        mock_path.isfile.return_value = False
        rm("haha")
        self.assertFalse(mock_os.remove.called)

        mock_path.isfile.return_value = True
        rm("haha")
        # check function call
        mock_os.remove.assert_called_with("haha")


class RemovalServiceTestCase(TestCase):
    """Test object method.
    Patch builtin module to modify behavior of buitlin methods."""

    @patch('pycool.example.util.os.path')
    @patch('pycool.example.util.os')
    def test_object_method_rm(self, mock_os, mock_path):
        reference = RemovalService()

        mock_path.isfile.return_value = False
        reference.rm("any path")
        self.assertFalse(mock_os.remove.called, "Failed to remove")

        mock_path.isfile.return_value = True
        reference.rm("any path")
        mock_os.remove.assert_called_with("any path")


class UploadServiceTestCase(TestCase):
    """Test object method: Patch another private module's object method."""

    @patch.object(RemovalService, 'rm')
    def test_upload_complete(self, mock_rm):
        """
        Note:
        1) `@patch.object(RemovalService, 'rm')` because we have
            `from pycool.example.util import RemovalService`
            in the import part; For `import pycool`, see next test suite.
        """
        removal_service = RemovalService()
        upload_service = UploadService(removal_service)
        upload_service.upload_complete("filename")

        # check that it called `rm` method of any RemovalService
        mock_rm.assert_called_with("filename")

        # check that it called `rm` method of `removal_service` instance
        removal_service.rm.assert_called_with("filename")


class UploadServiceImportTestCase(TestCase):
    """Test object method: How `import` goes with `@patch.object` part."""

    import pycool

    @patch.object(pycool.example.util.RemovalService, 'rm')
    def test_upload_complete_import_pycool(self, mock_rm):
        # because we hace `import pycool`, we can use
        # @patch.object(pycool.example.util.RemovalService, 'rm')
        removal_service = RemovalService()
        UploadService(removal_service).upload_complete("filename")
        mock_rm.assert_called_with("filename")


class UploadServiceMockInstance(TestCase):
    """Test object method: Mock instance with create_autospec."""

    def test_upload_mock_instance(self):

        mock_removal_service = mock.create_autospec(RemovalService)

        reference = UploadService(mock_removal_service)
        reference.upload_complete("upload complete")
        mock_removal_service.rm.assert_called_with("upload complete")
