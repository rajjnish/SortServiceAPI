import pytest
from conftest import post_req_sort, post_req_sort_rev
import json


@pytest.mark.sort_negative
@pytest.mark.parametrize(('input_list'), [([1, 2, 3, 4, '#$']),
                                          ([1, 2, 3, 4, 'a']),
                                          ([1, 2, 3, 4, 2.5]),
                                          ([1, 2, 3, 4, None]),
                                          ([None, None]),
                                          ([1, True, 2, False])])
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
                                          ([None, None]),
                                          ([1, True, 2, False])])
def test_sort_rev_request_neg(input_list):
    """sorting Reverse request - List values have incorrect data type, garbage values
        Primarily Non integer values"""
    payload = json.dumps({"list": input_list})
    response = post_req_sort_rev(payload)
    print(response.json())
    assert response.status_code == 401


@pytest.mark.sort_negative
def test_sort_asc_request_more_than_one_list():
    """sorting asc request - More than one list is sent in the Payload """
    payload = json.dumps({"list": [3, 2, 9, 1], "list1": [10, 2, 9, 1]})
    response = post_req_sort(payload)
    print(response.json())
    assert response.status_code == 401


@pytest.mark.sort_negative
def test_rev_asc_request_more_than_one_list():
    """sorting Reverse request - More than one list is sent in the Payload """
    payload = json.dumps({"list": [3, 2, 9, 1], "list1": [10, 2, 9, 1]})
    response = post_req_sort_rev(payload)
    print(response.json())
    assert response.status_code == 401


@pytest.mark.sort_negative
def test_sort_asc_request_neg_invalid_key():
    """sorting asc request - The Key's value of the payload is incorrect/unexpected """
    payload = json.dumps({"invalid": [3, 2, 9, 1]})
    response = post_req_sort(payload)
    print(response.json())
    assert response.status_code == 401


@pytest.mark.sort_negative
def test_sort_rev_request_neg_invalid_key():
    """sorting reverse request - The Key's value of the payload is incorrect/unexpected """
    payload = json.dumps({"invalid": [3, 2, 9, 1]})
    response = post_req_sort_rev(payload)
    print(response.json())
    assert response.status_code == 401
