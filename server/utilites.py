'''
Utility functions for application
'''

from os.path import join as join_paths
from typing import Callable
from uuid import uuid4

from django.db.models import Model



def build_upload_path(base_path: str) -> Callable[[Model, str], str]:
    def wrapper(instance: Model, source_file_name: str) -> str:
        file_suffix = source_file_name.split('.')[-1]
        new_file_name = f'{uuid4().hex}.{file_suffix}'
        return join_paths(base_path, new_file_name)
    return wrapper
