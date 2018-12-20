import pytest, api
from flask import json

@pytest.fixture
def client():
    '''define a test client'''
    with api.app.app_context():
        api.app.config['TESTING'] = True
        test_client = api.app.test_client()
    return test_client

