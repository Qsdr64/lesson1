import pytest
import requests

BASE_URL = "https://ru.yougile.com"
token = 'lrk4ZxM5WvOfpyHiQ3cBrjlwvW4GihDKlPL2PzbQeIUhZaia-nWpv+7-zX89BZag'
project_id_value = None
def test_project_id():
    global project_id_value 
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    json_data = {
        "title": "New_company"
    }
    resp = requests.post(f'{BASE_URL}/api-v2/projects', headers=headers, json=json_data)
    assert resp.status_code == 201
    response_json = resp.json()
    project_id_value = response_json.get('id')
    assert project_id_value is not None

def test_new_titel():
    global project_id_value
    header ={ 'Authorization': f'Bearer {token}',
              'Content-Type': 'application/json' 
              }
    data = {
        "title": "two_project"
        }
    res_project = requests.put(f'{BASE_URL}/api-v2/projects/{project_id_value}', headers=header, json=data)   
    assert res_project.status_code == 200
def test_id():
    global project_id_value
    header ={ 'Authorization': F'Bearer {token}',
              'Content-Type': 'application/json' 
              }
   
    res_project = requests.put(f'{BASE_URL}/api-v2/projects/{project_id_value}', headers=header,)   
    assert res_project.status_code == 200
def test_fail_company():
    global project_id_value 
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    json_data = {
        
    }
    resp = requests.post(f'{BASE_URL}/api-v2/projects', headers=headers, json=json_data)
    assert resp.status_code == 400
    response_json = resp.json()
def test_fail_new_titel():
    global project_id_value
    header ={ 'Authorization': f'Bearer {token}',
              'Content-Type': 'application/json' 
              }
    data = {
        
        }
    res_project = requests.put(f'{BASE_URL}/api-v2/projects/{project_id_value}', headers=header, json=data)   
    assert res_project.status_code == 400
def test_fail_id():
    global project_id_value
    header ={ 'Authorization': F'Bearer {token}',
              'Content-Type': 'application/json' 
              }
   
    res_project = requests.put(f'{BASE_URL}/api-v2/projects/{"21412342rwdfafwe1e1"}', headers=header,) 
    assert res_project == 404