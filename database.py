from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://dev2dreamer:dev2dreamer@marketreasearch.lqbhv.mongodb.net/?retryWrites=true&w=majority&appName=MarketReasearch"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# client = MongoClient("mongodb://localhost:27017")
db = client.market_research

def insert_company_info(data):
    db.company_info.insert_one(data)

def insert_use_case(data):
    db.use_cases.insert_one(data)

def insert_datasets(data):
    db.datasets.insert_one(data)

def log_request(data):
    db.logs.insert_one(data)
