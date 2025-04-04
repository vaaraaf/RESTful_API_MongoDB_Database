import requests

##*************Insert One Item*************
# URL_insert_one = 'http://127.0.0.1:5000'
# data_insert_one = {'NAME': 'Sample_name'}
# response = requests.post(url=URL_add_one, json=data_insert_one)


##*************Adding Many Item*************
URL_insert_many = 'http://127.0.0.1:5000/add_many'
data_insert_many = [{'NAME': 'Sample1', 'age': 91, 'city': 'Georgia'},
                    {'NAME': 'Sample2', 'age': 92, 'city': 'Austin'},
                    {'NAME': 'Sample3', 'age': 93, 'city': 'Irvine'}]
response = requests.post(url=URL_insert_many, json=data_insert_many)


##*************Query One*************
# URL_query_one = 'http://127.0.0.1:5000/query_one'
# data = {'NAME': 'Sample1'}
# response = requests.post(URL_query_one, json=data)

##*************Query All*************
# URL_query_all = 'http://127.0.0.1:5000/query_all'
# data = {'NAME': 'Sample1'}
# response = requests.post(URL_query_all, json=data)


##*************Update One*************
# URL_update_one = 'http://127.0.0.1:5000/update_one'
# update_one_criteria = {'criteria': {'NAME': 'Sample1'}, 'function': {'$set': {'age': 800}}}
# response = requests.post(URL_update_one, json=update_one_criteria)

##*************Aggregation Pipeline*************
# URL_aggregation = 'http://127.0.0.1:5000/aggregation'
# aggregation_pipeline = {'$group': {'_id': '$city', 'average_age': {'$avg':'$age'}}}
# response = requests.post(URL_aggregation, json=aggregation_pipeline)


##*************Delete One*************
# URL_delete_one = 'http://127.0.0.1:5000/delete_one'
# delete_one_criteria = {'NAME': 'Sample1'}
# response = requests.post(URL_delete_one, json=delete_one_criteria)


##*************Delete Many*************
# URL_delete_many = 'http://127.0.0.1:5000/delete_many'
# delete_many_criteria = {'NAME': 'Sample2'}
# response = requests.post(URL_delete_many, json=delete_many_criteria)



print('Status Code', response.status_code)
print('Response:', response.json())
