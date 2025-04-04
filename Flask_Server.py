from flask import Flask, jsonify, request
import MongoDB_Connection

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return jsonify({'Message': 'Welcome'})


@app.route('/', methods=['POST'])
def insert_one_item():
    new_item = request.get_json()
    add_record = MongoDB_Connection.insert_one_doc(new_item)
    if add_record:
        print('Data Successfully Added!')
        return jsonify(str(new_item))           # the MongoDB changes the new_item in-place and adds the id object to it.
    return jsonify({'Warning': 'Data is not uploaded'})


@app.route('/add_many', methods=['POST'])
def insert_many_item():
    list_of_new_item = request.get_json()
    print(f'list of new = {list_of_new_item}')
    add_record = MongoDB_Connection.insert_many_doc(list_of_new_item)
    print(add_record)
    return jsonify(str(add_record))


@app.route('/query_one', methods=['POST'])
def get_one_query():
    criteria = request.get_json()
    result = MongoDB_Connection.find_one_doc(criteria)
    return jsonify(str(result))


@app.route('/query_all', methods=['POST'])
def get_all_query():
    criteria = request.get_json()
    print(criteria)
    results = MongoDB_Connection.find_all_doc(criteria)
    # print(list(results))
    return jsonify(str(results))


@app.route('/update_one', methods=['POST'])
def update_one_doc():
    criteria = request.get_json()
    print(criteria)
    result = MongoDB_Connection.find_and_update_one_doc(criteria)
    print(f'result is {result}')
    return jsonify(str(result))


@app.route('/aggregation', methods=['POST'])
def aggregate_pipeline():
    criteria = request.get_json()
    result = MongoDB_Connection.aggregate_pipeline([criteria])
    print(result)
    return jsonify(result)


@app.route('/delete_one', methods=['POST'])
def delete_one_doc():
    criteria = request.get_json()
    result = MongoDB_Connection.find_and_delete_one_doc(criteria)
    print(f'outside {result}')
    return jsonify(str(result))


@app.route('/delete_many', methods=['POST'])
def delete_many_doc():
    criteria = request.get_json()
    result = MongoDB_Connection.delete_many_doc(criteria)
    return jsonify(str(result))


if __name__ == '__main__':
    app.run(debug=True)