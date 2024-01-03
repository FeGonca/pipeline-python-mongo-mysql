from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests


def connect_mongo(uri):
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        return client
    except Exception as e:
        return e

def create_connect_db(client, db_name):
    db = client[db_name]
    return db

def create_connect_collection(db, col_name):
    return db[col_name] 

def extract_api_data(url):
    return requests.get(url).json()

def insert_data(col, data):
    docs = col.insert_many(data)
    return len(docs.inserted_ids)

if __name__ == '__main__':
    
    client = connect_mongo("mongodb+srv://felipe:felipe@cluster0.nfkmkmi.mongodb.net/?retryWrites=true&w=majority")
    db = create_connect_db(client, "db_produtos_desafio")
    col = create_connect_collection(db, "produtos")

    data = extract_api_data("https://labdados.com/produtos")
    print(f"\nQuantidade de dados extraidos: {len(data)}")

    n_docs = insert_data(col, data)
    print(f"\nDocumentos inseridos na colecao: {n_docs}")

    client.close()
