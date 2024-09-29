import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def MongoDb_Connect(uri):
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)

def create_DB(client,dataPath):

    cleaned_data = pd.read_csv(dataPath)
    db = client['SecurityData']  
    collection = db['ipAddress']  

    #Prepare Data for Insertion
    records = cleaned_data.to_dict(orient='records')
    #Insert Data into MongoDB
    collection.insert_many(records)

    #Create an index on the ip_address field
    collection.create_index('ip_address', unique=True)

    # Verify Data and Indexing
    print(f"Number of documents in collection: {collection.count_documents({})}")
    print("Indexes in the collection:", collection.index_information())


if __name__ == "__main__":
    uri = "mongodb+srv://sukumaran1004:4U9q6quOS9PhJiLS@threatsecurity.r95nm.mongodb.net/?retryWrites=true&w=majority&appName=ThreatSecurity"
    cleaned_data = 'Data/Cleaned_Data.csv'
    client = MongoDb_Connect(uri)
    create_DB(client,cleaned_data)