import pymongo

# MongoDB Properties
MONGO_HOST_URL = "mongodb://127.0.0.1:27017/"
MONGO_DB_NAME    = "py24db"
MONGO_CLIENT_OB  = None
MONGO_DB_OB      = None


def get_mongodb_connection():
    global MONGO_CLIENT_OB
    global MONGO_DB_OB
    if MONGO_CLIENT_OB is None:
        MONGO_CLIENT_OB = pymongo.MongoClient(MONGO_HOST_URL)
        MONGO_DB_OB  = MONGO_CLIENT_OB[MONGO_DB_NAME]
        print("MongoDB Connected....")
        return MONGO_CLIENT_OB


def close_mongodb_connection():
    global MONGO_CLIENT_OB
    global MONGO_DB_OB

    if MONGO_CLIENT_OB is not None:
        MONGO_CLIENT_OB.close()
        MONGO_CLIENT_OB = None
        MONGO_DB_OB = None
        print("MongoDB Dis-Connected....")

def get_collection(cname): # cname ="student"
    if MONGO_DB_OB is not None:
        return MONGO_DB_OB[cname]
