import pytest
from conftest import post_req_sort, post_req_sort_rev
import json
import requests


@pytest.mark.sort_negative
@pytest.mark.parametrize(('input_list'), [([1, 2, 3, 4, '#$']),
                                          ([1, 2, 3, 4, 'a']),
                                          ([1, 2, 3, 4, 2.5]),
                                          ([1, 2, 3, 4, None]),
                                          ([None, None])])
def test_sort_asc_request_neg(input_list):
    """sorting asc request - List values have incorrect data type, garbage values
        Primarily Non integer values"""
    payload = json.dumps({"list": input_list})
    response = post_req_sort(payload)
    print(response.json())
    assert response.status_code == 401


@pytest.mark.sort_negative
@pytest.mark.parametrize(('input_list'), [([1, 2, 3, 4, '#$']),
                                          ([1, 2, 3, 4, 'a']),
                                          ([1, 2, 3, 4, 2.5]),
                                          ([1, 2, 3, 4, None]),
                                          ([None, None])])
def test_sort_rev_request_neg(input_list):
    """sorting Reverse request - List values have incorrect data type, garbage values
        Primarily Non integer values"""
    payload = json.dumps({"list": input_list})
    response = post_req_sort_rev(payload)
    print(response.json())
    assert response.status_code == 401


@pytest.mark.sort_negative
def test_sort_asc_request_neg2():
    """sorting asc request - The Key's value of the payload is incorrect/unexpected """
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
