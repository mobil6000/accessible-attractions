from django.db.models import Model
from pytest import fixture

from server.utilites import build_upload_path



@fixture
def fake_django_model() -> Model:
    class FakeModel(Model):
        class Meta:
            app_label = 'main'

    return FakeModel()


def test_build_upload_path(fake_django_model: Model) -> None:
    fake_upload_dir_name = 'downloads'
    result_function = build_upload_path(fake_upload_dir_name)
    expected_path = result_function(fake_django_model, 'file1.docx')
    assert expected_path.startswith(fake_upload_dir_name)
    assert expected_path.endswith('docx')
