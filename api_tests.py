import pytest, api
from flask import json

@pytest.fixture
def client():
    '''define a test client'''
    with api.app.app_context():
        api.app.config['TESTING'] = True
        test_client = api.app.test_client()
    return test_client

class TestApi():
    def test_create_redflag(self, client):
        red_flag = {
            'id' : 1,
            'title' : 'Bribery',
            'latitude': 372823,
            'longitude': 363837,
            'Description': 'there is a need to learn this thing'
        }
        url = '/api/v1/redflags'
        resp = client.post(url, data=json.dumps(red_flag), content_type='application/json')
        assert red_flag in api.all_redflags
        assert resp.json['status'] == 201