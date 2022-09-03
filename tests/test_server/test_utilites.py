from typing import Any, Callable

from django.db import Error as DBError
from django.db.models import Model
from pytest import fixture, raises

from server.utilites import build_upload_path, BusinessLogicFailure, handle_db_errors, md_to_html



@fixture
def fake_django_model() -> Model:
    class FakeModel(Model):
        class Meta:
            app_label = 'main'

    return FakeModel()


@fixture
def fake_db_query() -> Callable[..., None]:
    def func():
        raise DBError('error!')
    return func


def test_build_upload_path(fake_django_model: Model) -> None:
    fake_upload_dir_name = 'downloads'
    expected_path = build_upload_path(fake_django_model, 'file1.docx', fake_upload_dir_name)
    assert expected_path.startswith(fake_upload_dir_name)
    assert expected_path.endswith('docx')


def test_md_to_html() -> None:
    expected_result = '<p><strong>Text! </strong></p>'
    real_result = md_to_html('**Text! **')
    assert expected_result == real_result


def test_handle_db_errors(fake_db_query: Callable[..., None]) -> None:
    fake_service_function = handle_db_errors(fake_db_query)
    with raises(BusinessLogicFailure):
        fake_service_function()
