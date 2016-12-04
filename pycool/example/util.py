import os
import os.path


class RemovalService(object):
    """A service for removing objects from the filesystem."""

    MY_MODULE_CONSTANT = 1

    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)

    def done(self):
        return True

    @classmethod
    def finish(cls):
        return 0


class UploadService(object):
    """A upload service."""

    def __init__(self, removal_service):
        self.removal_service = removal_service

    def upload_complete(self, filename):
        self.removal_service.rm(filename)


def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)
