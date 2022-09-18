import re

from django.test import Client
from pytest import fixture



@fixture()
def page_title() -> str:
    '''
    Returns pattern for the page title
    '''

    return r' *<title>Мир путешествий и возможностей</title>'


@fixture()
def main_content() -> str:
    '''
    Returns pattern for basic information on the page
    '''

    return (
        r'<p.*>\n*'
        ' *Проект «Мир путешествий и возможностей» представляет собой '
        r'справочник музеев, усадеб, скверов, театров доступных для посещения незрячими людьми.\n*'
        r' *На сайте слепые и слабовидящие пользователи смогут найти маршрут до '
        r'20 объектов культуры от ближайшей станции метро, позволяющий добраться без '
        r'посторонней помощи, аудио с описанием доступных для тактильного '
        r'ознакомления экспонатов каждого из представленных музеев.\n*'
        r' *Проект создан при поддержке конкурса грантов «Москва – добрый город».\n*'
        '</p>'
    )


def test_main_page_status(client: Client) -> None:
    '''
    This test ensures that url of the main page returns correct status
    '''

    response = client.get('/')
    assert response.status_code == 200


def test_main_page_content(client: Client, page_title: str, main_content: str) -> None:
    '''
    This test ensures that url of the main page returns correct page content
    '''

    response = client.get('/')
    page_content = response.content.decode()
    assert re.search(page_title, page_content)
    assert re.search(main_content, page_content)
