import sys, os
import jsonschema
from jsonschema import validate
import requests

BASE_URL = "http://localhost:5000"

POST_SORT_ENDPOINT = "/v1/sort"
POST_SORT_REV_ENDPOINT = "/v1/reverse"
DEFAULT_TIMEOUT = 5

root_dir = os.path.dirname(os.path.abspath(__file__))

SCHEMA = {
    "type": "object",
    "properties": {
        "list": {"type": "Array"},
    }
}


def get_req():
    """ Get request to the root endpoint"""
    response = requests.get(BASE_URL, timeout=DEFAULT_TIMEOUT)
    assert response.status_code == 200


def post_req_sort(data=None):
    """ Get request to the sort endpoint"""
    response = requests.post(BASE_URL + POST_SORT_ENDPOINT, json=data, timeout=DEFAULT_TIMEOUT)
    return response


def post_req_sort_rev(data):
    """ Get request to the reverse endpoint"""
    response = requests.post(BASE_URL + POST_SORT_REV_ENDPOINT, json=data, timeout=DEFAULT_TIMEOUT)
    return response


def schema_validate(schema, data):
    for index, item in enumerate(data):
        try:
            validate(item, schema)
            sys.stdout.write("Schema of response data #{}: OK\n".format(index))
            return True
        except jsonschema.exceptions.ValidationError as ve:
            sys.stderr.write("Schema of response data #{}: ERROR\n".format(index))
            sys.stderr.write(str(ve) + "\n")
            return False
