from functools import wraps
from typing import Any, Callable, NewType

from django.db import Error as DBError
from result import Err, Result



ErrorReason = NewType('ErrorReason', str)


def catch_database_errors(func: Callable[..., Any]):
    @wraps(func)
    def wrapper(*args, **kwargs) -> Result[Any, ErrorReason]:
        try:
            result_value = func(*args, **kwargs)
        except DBError as catched_exception:
            msg = str(catched_exception)
            return Err(ErrorReason(msg))
        return result_value

    return wrapper
