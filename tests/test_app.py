import pytest
from app import create_app, db
from app.models import Post

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Posts' in response.data

def test_add_post(client):
    response = client.post('/add', data={'title': 'Test', 'content': 'Test content'})
    assert response.status_code == 302  # redirect
    # Check if post was added
    with client.application.app_context():
        post = Post.query.first()
        assert post.title == 'Test'