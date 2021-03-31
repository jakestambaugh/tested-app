from main import app
import json


def test_homepage_displays():
    client = app.test_client()
    response = client.get("/")
    assert response.get_json() == {"hello": "world"}

def test_form_jumping_jack():
    client = app.test_client()
    response = client.post("/form", data={"foo": "jumping", "bar": "jack"})
    assert response.headers["X-foo-bar"] == "jumping; jack"

def test_form_kitty_cat():
    client = app.test_client()
    response = client.post("/form", data={"foo": "kitty", "bar": "cat"})
    assert response.headers["X-foo-bar"] == "kitty; cat"

def test_not_found():
    client = app.test_client()
    response = client.get("/not/a/real/path")
    assert response.status_code == 404
