import pytest
from conftest import post_req_sort
import json


@pytest.mark.sort_asc_positive
@pytest.mark.parametrize(('input_list', 'exp_res'),[([10, 5, 18, 35, 4, 78], [4, 5, 10, 18, 35, 78]),
                                               ([12,1,9], [1, 9, 12]),
                                               ([-1, -2, 1, 2], [-2, -1, 1, 2]),
                                                    ([], []),
                                                    ([2], [2]),
                                                    ([-2147483647, -2147483648, 2147483648, 2147483647],
                                                     [-2147483648, -2147483647, 2147483647, 2147483648])])
def test_sort_asc_request(input_list, exp_res):
    """sorting asc request - data driven test"""
    payload = json.dumps({"list": input_list})
    response = post_req_sort(payload)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['sorted_list'] == exp_res

