'''
Utility functions for application
'''

from os.path import join as join_paths
from uuid import uuid4

from django.db.models import Model
from markdown import markdown



def build_upload_path(instance: Model, source_file_name: str, base_path: str | None=None) -> str:
    file_suffix = source_file_name.split('.')[-1]
    new_file_name = f'{uuid4().hex}.{file_suffix}'
    if base_path is not None:
        return join_paths(base_path, new_file_name)
    else:
        return new_file_name


def md_to_html(source: str) -> str:
    return markdown(source)
