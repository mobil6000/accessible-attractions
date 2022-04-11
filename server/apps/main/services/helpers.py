from typing import NewType

from returns.pipeline import is_successful



ErrorReason = NewType('ErrorReason', str)
is_successful_result = lambda container: is_successful(container)
