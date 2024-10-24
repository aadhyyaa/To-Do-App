import pytest
from flask import url_for
from app import app, todos

@pytest.fixture(autouse=True)
def run_before_tests():
    todos.clear()

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'To-Do List' in response.data

def test_add_task(client):
    response = client.post('/add-task', data = {'todo': 'New task'}, follow_redirects = True)
    assert response.status_code == 200
    assert b'New task' in response.data

def test_edit_task(client):
    client.post('/add-task', data = {'todo': 'New task to EDIT', 'done':False}, follow_redirects = True)
    response = client.post('/edit-task/0', data = {'todo': 'Edited task', 'done':False}, follow_redirects = True)
    assert response.status_code == 200
    assert b'Edited task' in response.data

def test_check(client):
    client.post('/add-task', data = {'todo': 'Check task', 'done':False}, follow_redirects = True)
    response = client.get('/check/0', follow_redirects = True)
    assert response.status_code == 200
    assert b'checked' in response.data

def test_delete(client):
   client.post('/add-task', data={'todo': 'Delete task'}, follow_redirects=True)
   response = client.get('/delete/0', follow_redirects=True)
   response_after_delete = client.get('/', follow_redirects=True)
   assert response_after_delete.status_code == 200
   assert b'Delete task' not in response_after_delete.data 

