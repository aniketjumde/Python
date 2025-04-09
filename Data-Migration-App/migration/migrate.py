from config.csvconf.configuration import FILENAME
from config.mongodb.configuration import get_collection
from student.load import load_from_csv, load_from_sqldb, load_from_mongodb, load_from_user
from student.save import save_to_sqldb, save_to_mongodb, save_to_csv


def csv_to_sqldb(filepath, tablename):
    L = load_from_csv(filepath)
    save_to_sqldb(tablename, L)
    print(f"Migration from CSV File :{filepath} to Table:{tablename} is Successfully !!!")

def csv_to_mongodb(filepath, collection_name):
    L = load_from_csv(filepath)
    save_to_mongodb(collection_name,L)
    print(f"Migration from CSV File :{filepath} to Collection:{collection_name} is Successfully !!!")

def sqldb_to_csv(tablename, filepath):
    L = load_from_sqldb(tablename)
    save_to_csv(filepath, L)
    print(f"Migration from Table :{tablename} to CSV:{filepath} is Successfully !!!")

def sqldb_to_mongodb(tablename, collection_name):
    L = load_from_sqldb(tablename)
    save_to_mongodb(collection_name, L)
    print(f"Migration from Table :{tablename} to Collection:{collection_name} is Successfully !!!")

def mongodb_to_csv(collection_name, filepath):
    L = load_from_mongodb(collection_name)
    save_to_csv(filepath, L)
    print(f"Migration from Collection :{collection_name} to CSV:{filepath} is Successfully !!!")

def mongodb_to_sqldb(collection_name, tablename):
    L = load_from_mongodb(collection_name)
    save_to_sqldb(tablename, L)
    print(f"Migration from Collection :{collection_name} to Table:{tablename} is Successfully !!!")

def user_input_to_csv(n,filepath):
    L = load_from_user(n)
    save_to_csv(filepath, L)
    print(f"Data Saved in CSV '{filepath}'")

def user_input_to_sqldb(n, tablename):
    L = load_from_user(n)
    save_to_sqldb(tablename, L)
    print(f"Data is Saved in Table :'{tablename}' ")

def user_input_to_mongodb(n, collection_name):
    L = load_from_user(n)
    save_to_mongodb(collection_name, L)
    print(f"Data is Saved in Collection :'{collection_name}' ")