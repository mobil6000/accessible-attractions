from django.db.models import Model
from pytest import fixture

from server.utilites import build_upload_path, md_to_html



@fixture
def fake_django_model() -> Model:
    class FakeModel(Model):
        class Meta:
            app_label = 'main'

    return FakeModel()


def test_build_upload_path(fake_django_model: Model) -> None:
    fake_upload_dir_name = 'downloads'
    expected_path = build_upload_path(fake_django_model, 'file1.docx', fake_upload_dir_name)
    assert expected_path.startswith(fake_upload_dir_name)
    assert expected_path.endswith('docx')


def test_md_to_html() -> None:
    expected_result = '<p><strong>Text! </strong></p>'
    real_result = md_to_html('**Text! **')
    assert expected_result == real_result
