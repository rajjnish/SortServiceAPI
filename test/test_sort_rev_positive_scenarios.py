import pytest
from conftest import post_req_sort_rev
import json


@pytest.mark.sort_rev_positive
@pytest.mark.parametrize(('input_list', 'exp_res'),[([10, 5, 18, 35, 4, 78], [78, 35, 18, 10, 5, 4]),
                                               ([12,1,9], [12,9,1]),
                                               ([-1, -2, 1, 2], [2, 1, -1, -2])])
def test_sort_asc_request(input_list, exp_res):
    """sorting asc request"""
    payload = json.dumps({"list": input_list})
    response = post_req_sort_rev(payload)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['sorted_list'] == exp_res