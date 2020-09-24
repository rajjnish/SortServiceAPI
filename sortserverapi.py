from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    """ Root Endpoint for GET request """
    return jsonify({"server": 'sorting service api', "status": "success"})


def sort_list_asc(list_no):
    return sorted(list_no)


def sort_list_rev(list_no):
    return sorted(list_no, reverse=True)


def verify_non_integer_list(input_list):
    """ returns True if all list items are integer else False"""
    for e in input_list:
        if type(e) != int:
            return False
        else:
            continue
    return True


def err_out(data):
    return {'status': 'invalid input', 'you sent': data}


@app.route('/v1/sort', methods=['POST'])
def sort_list():
    """sort endpoint to send Simple Asc order Sorting request """
    data = request.get_json()
    data_j = json.loads(data)
    key_val = list(data_j.keys())

    if len(data_j['list']) <= 1:
        return jsonify({"status": "success", 'sorted_list': data_j['list']})

    if key_val[0] != 'list':
        out = err_out(data_j)
        response = jsonify(out), 401
        return response

    data_list = json.loads(data)['list']
    check_input_list = verify_non_integer_list(data_list)
    # Check if all elements in the list are integer
    if check_input_list:
        sorted_list = sort_list_asc(data_list)
        return jsonify({"status": "success", 'sorted_list': sorted_list})
    else:
        out = err_out(data_j)
        response = jsonify(out), 401
        return response


@app.route('/v1/reverse', methods=['POST'])
def sort_list_reverse():
    """reverse endpoint to send Sorting request for sorting request with Reverse True"""
    data = request.get_json()
    data_j = json.loads(data)
    key_val = list(data_j.keys())

    if len(data_j['list']) <= 1:
        return jsonify({"status": "success", 'sorted_list': data_j['list']})

    if key_val[0] != 'list':
        out = err_out(data_j)
        response = jsonify(out), 401
        return response

    data_list = json.loads(data)['list']
    check_input_list = verify_non_integer_list(data_list)
    # Check if all elements in the list are integer
    if check_input_list:
        sorted_list = sort_list_asc(data_list)
        return jsonify({"status": "success", 'sorted_list': sorted_list})
    else:
        out = err_out(data_j)
        response = jsonify(out), 401
        return response


@app.route('/v1/test', methods=['POST'])
def sort_list_test():
    """sort endpoint to send Simple Asc order Sorting request """
    data = request.get_json()
    data_j = json.loads(data)
    key_val = list(data_j.keys())
    # if len(json.loads(data)['list']) == 0:
    #     out = err_out(data)
    #     response = jsonify(out), 401
    #     return response
    # elif len(json.loads(data)[0]) != 'list':
    #     response = jsonify("{'status': 'invalid input', 'you sent': data}"), 401
    #     return response
    #
    # data_list = json.loads(data)['list']
    # sorted_list = sort_list_asc(data_list)
    #
    # return jsonify({"status": "success", 'sorted_list': sorted_list})
    return {'status': 'invalid input', 'you sent': key_val[0]}


if __name__ == '__main__':
    app.run(debug=True)
