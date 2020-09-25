from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    """ Root endpoint for GET request """
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


def json_data_dict(data):
    return json.loads(data)


def dict_keys_list(input_dict):
    return list(input_dict.keys())


def err_out(data):
    return {'status': 'invalid input', 'you sent': data}


@app.route('/v1/sort', methods=['POST'])
def sort_list():
    """sort endpoint to send Simple Asc order Sorting request """
    data = request.get_json()
    data_j = json_data_dict(data)
    key_val = dict_keys_list(data_j)

    if key_val[0] != 'list':
        out = err_out(data_j)
        response = jsonify(out), 401
        return response

    if len(data_j['list']) <= 1:
        return jsonify({"status": "success", 'sorted_list': data_j['list']})

    if len(data_j) >= 2:
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
    """reverse endpoint to send Sorting request with Reverse True"""
    data = request.get_json()
    data_j = json_data_dict(data)
    key_val = dict_keys_list(data_j)

    if key_val[0] != 'list':
        out = err_out(data_j)
        response = jsonify(out), 401
        return response

    if len(data_j['list']) <= 1:
        return jsonify({"status": "success", 'sorted_list': data_j['list']})

    if len(data_j) >= 2:
        out = err_out(data_j)
        response = jsonify(out), 401
        return response

    data_list = json.loads(data)['list']
    check_input_list = verify_non_integer_list(data_list)
    # Check if all elements in the list are integer
    if check_input_list:
        sorted_list = sort_list_rev(data_list)
        return jsonify({"status": "success", 'sorted_list': sorted_list})
    else:
        out = err_out(data_j)
        response = jsonify(out), 401
        return response


if __name__ == '__main__':
    app.run(debug=True)
