class BaseAppException(Exception):
    """The base class of all TDL Errors"""

class TDL_AttributeError(BaseAppException):
    """Errors refered to exception in task and collection attributs(names, descriptions)"""
    
class TDL_ObjectNotFoundError(BaseAppException):
    """Errors reffered to objects that does not exist in the database."""

class TDL_ObjectDuplicationError(BaseAppException):
    """Errors referred to object duplication and repitition such as Task objects and Collection objects."""

class TDL_CollectionFullError(BaseAppException):
    """Raised when we call the createTask() function in the Collection class when the class is full."""
