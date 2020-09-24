import pytest
from conftest import post_req_sort
import json
import requests




@pytest.mark.sort_negative
def test_sort_asc_request_neg1():
    """sorting asc request"""
    payload = json.dumps({"list": []})
    response = post_req_sort(payload)
    print(response.json())
    assert response.status_code == 401
    assert response.json()['status'] == "invalid input"


@pytest.mark.sort_negative
def test_sort_asc_request_neg2():
    """sorting asc request"""
    payload = json.dumps({"invalid": [3, 2, 9, 1]})
    response = post_req_sort(payload)
    print(response.json())
    # assert response.status_code == 401
    # assert response.json()['status'] == "invalid input"

def test_sort_asc_request1():
    """sorting asc request"""
    # assert response.json()['sorted_list'] == exp_res
    BASE_URL = "http://localhost:5000"
    POST_SORT_ENDPOINT = "/v1/test"
    payload = json.dumps({"invalid": [3, 2, 9, 1]})
    response = requests.post(BASE_URL + POST_SORT_ENDPOINT, json=payload)
    print(response.json())
    assert response.json()['you sent'] != list
    # assert response.status_code == 401