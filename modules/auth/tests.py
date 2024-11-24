from fastapi.testclient import TestClient

from alchemy.queries.user_queries import delete_user
from main import app

client = TestClient(app)

def test_login():
    response = client.post('/api/auth/login', json={
        'login': 'string',
        'password': 'string'
    })

    assert response.status_code == 200
    assert response.json().get('user') is not None
    assert response.json().get('token') is not None
    print('test_login - ok')

def test_register():
    response = client.post('/api/auth/register', json={
        "nickname": "test1",
        "login": "test1",
        "password": "test1",
        "email": "test@example.com"
    })

    user = response.json().get('user')
    id = user.get('id')
    delete_user(id)
    assert response.status_code == 200
    assert response.json().get('user') is not None
    assert response.json().get('token') is not None

    print('test_register - ok')

def test_logout():
    response = client.post('/api/auth/login', json={
        'login': 'string',
        'password': 'string'
    })
    access_token = response.json().get('token').get('access_token')

    response = client.post('/api/auth/logout', headers={"Authorization": f"Bearer {access_token}"})
    assert response.status_code == 200
    assert response.json().get('status') is not None
    print('test_logout - ok')

test_login()
test_register()
test_logout()

