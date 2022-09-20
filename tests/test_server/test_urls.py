from django.test import Client



def test_robots_txt(client: Client) -> None:
    '''
    This test ensures that `robots.txt` is accessible.
    '''

    response = client.get('/robots.txt')
    assert response.status_code == 200
    assert response.get('Content-Type') == 'text/plain'


def test_humans_txt(client: Client) -> None:
    '''
    This test ensures that `humans.txt` is accessible.
    '''

    response = client.get('/humans.txt')
    assert response.status_code == 200
    assert response.get('Content-Type') == 'text/plain'
