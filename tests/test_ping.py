from app import main
import logging

def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200

def test_meaning(test_app):
    response = test_app.get("/words/గాణ")
    logging.info(f"the meaning we got is: {response.text}")
    assert response.status_code == 200

def test_sentence(test_app):
    response = test_app.get("/simplesentence/?sentence=గాణ స్వాజన్యము abc")
    logging.info(f"the dictionary list we get is {response.text}")
    assert response.status_code == 200