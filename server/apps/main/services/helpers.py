from typing import Any, Callable, NewType

from django.db import Error as DBError
from result import Err



ErrorReason = NewType('ErrorReason', str)


def catch_database_errors(func: Callable[..., Any]):
    def wrapper(*args, **kwargs) -> Err[ErrorReason]:
        try:
            func(*args, **kwargs)
        except DBError as catched_exception:
            msg = str(catched_exception)
        return Err(ErrorReason(msg))

    return wrapper
