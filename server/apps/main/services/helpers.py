from typing import final, NewType



ErrorReason = NewType('ErrorReason', str)


@final
class DataMissingError(Exception):
    '''Exception raising in the absence of the requested data'''

    def __init__(self, error_message: str):
        self.message = error_message
        super().__init__(self, error_message)


    def __str__(self) -> str:
        return 'DataMissingError: {0}'.format(self.message)
