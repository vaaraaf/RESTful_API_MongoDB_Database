from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
USERNAME = 'Your_Username'
PASSWORD = 'Your_Password'
CLUSTER_NAME = 'Your_Cluster_name'
uri = f"mongodb+srv://{USERNAME}:{PASSWORD}@{CLUSTER_NAME}.hjeubfd.mongodb.net/?retryWrites=true&w=majority&appName=MyCluster"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client['Flask']
collection = db['users']


def insert_one_doc(one_document):
    insert_result = collection.insert_one(one_document)
    print(f'Inserted Document id:{insert_result.inserted_id}')
    return True


def insert_many_doc(list_of_documents):
    cursor = collection.insert_many(list_of_documents)
    results = cursor
    # print(f'Inserted Documents ids: {results}')
    return results


def find_one_doc(criteria_dictionary):
    person = collection.find_one(criteria_dictionary)
    # print(person)
    return person


def find_all_doc(criteria_dictionary):
    cursor = collection.find(criteria_dictionary)  #Note: The cussors from MongoDB are Lazy. You can convert them to a list only once.
    results = list(cursor)                         # Storing the data of the cursor into a list and later on we use this list. (The cursor is consumed here)
    for doc in results:
        print(doc)
    return results


def find_and_update_one_doc(criteria):
    cursor = collection.find_one_and_update(criteria['criteria'], criteria['function'])
    # result = cursor
    print(cursor)
    return cursor


def aggregate_pipeline(pipeline):
    aggregation_results = collection.aggregate(pipeline)
    results = list(aggregation_results)
    print('Aggregation Results:')
    for item in results:
        print(item)
    return results


def delete_one_doc(criteria):
    collection.delete_one(criteria)
    print(f'Deleted document {criteria}')


def find_and_delete_one_doc(criteria):
    cursor = collection.find_one_and_delete(criteria)
    print(cursor)
    return cursor


def delete_many_doc(criteria):
    cursor = collection.delete_many(criteria)
    print(cursor.deleted_count)
    return cursor


def drop_collection():
    collection.drop()
    print('Collection Dropped!')


if __name__ == '__main__':
    # drop_collection()
    # insert_one_doc({'name': 'VooVoo'})
    pass