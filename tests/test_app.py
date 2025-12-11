import app.app as flask_app

def test_home():
    response = flask_app.app.test_client().get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data
