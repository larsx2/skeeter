class SkeeterError(Exception):
    """Base Error Exception"""

class TargetPathError(SkeeterError):
    """Error related to target path"""

class BadPermissions(TargetPathError):
    """Target path is not readable"""
