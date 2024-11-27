from fastapi.testclient import TestClient

from modules.users.auth.queries import delete_user
from main import app

client = TestClient(app)

test_user = {
        "nickname": "test_user",
        "login": "test_user",
        "password": "test_user",
        "email": "test@example.com"
    }

def test_register():
    response = client.post('/api/auth/register', json=test_user)

    assert response.status_code == 200
    assert response.json().get('user') is not None
    assert response.json().get('user').get('password') is None
    assert response.json().get('token') is not None

    print('test_register - ok')

def test_login():
    response = client.post('/api/auth/login', json=test_user)
    print(response.json())
    assert response.status_code == 200
    assert response.json().get('user') is not None
    assert response.json().get('user').get('password') is None
    assert response.json().get('token') is not None
    print('test_login - ok')

def test_logout():
    response = client.post('/api/auth/login', json=test_user)
    access_token = response.json().get('token').get('access_token')
    user_id = response.json().get('user').get('id')
    response = client.post('/api/auth/logout', headers={"Authorization": f"Bearer {access_token}"})
    delete_user(user_id)
    assert response.status_code == 200
    assert response.json().get('status') is not None

    print('test_logout - ok')




