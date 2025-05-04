from pymongo import MongoClient
from utils import config

def get_mongo_client():
    return MongoClient(config.MONGO_URI)

def save_to_mongo(collection_name, dataframe):
    client = get_mongo_client()
    db = client[config.MONGO_DB]
    collection = db[collection_name]
    collection.drop()
    collection.insert_many(dataframe.to_dict('records'))
