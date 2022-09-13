'''
Utility tools for the application
'''

from functools import wraps
from hashlib import md5
from os.path import join as join_paths
from os.path import splitext
from typing import Any, Callable

from django.db import Error as DBError
from django.db.models import Model
from markdown import markdown



class BusinessLogicFailure(Exception):
    '''
    Raises by an error related to business scenarios
    '''
    pass



def build_upload_path(instance: Model, source_file_name: str, base_path: str | None=None) -> str:
    '''
    Generates a new path for uploaded media files
    '''

    main_file_name, file_suffix = splitext(source_file_name)
    main_file_name = md5(main_file_name.encode()).hexdigest()
    new_file_name = f'{main_file_name}{file_suffix}'
    if base_path is not None:
        return join_paths(base_path, new_file_name)
    else:
        return new_file_name


def md_to_html(source: str) -> str:
    '''
    Translates markdown into html markup
    '''

    return markdown(source)


def handle_db_errors(func: Callable[..., Any]):
    '''
    Wraps a function that interacts with database
    Raises an exception <Business Logic Failure>
    '''

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            result_value = func(*args, **kwargs)
        except DBError as catched_exception:
            raise BusinessLogicFailure(catched_exception)
        return result_value

    return wrapper
