import os

from skeeter import exception

class CmdLineRunner(object):
    """Command Line Runner"""

    def __init__(self, path, verbose=False, types=None):

        if not os.path.isdir(path):
            raise exception.TargetPathError("Target path is not a directory")

        if not os.access(path, os.R_OK):
            raise exception.BadPermissions("Target path is not readable")

        self.path = path
        self.types = 'all' if types is None else types
        self.verbose = verbose

    

