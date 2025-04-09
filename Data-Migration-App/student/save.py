import csv

from config.mongodb.configuration import get_collection
from config.mysqldb import get_mysqldb_connection

'''
    @Author : Sachin Dhane
    @Date   : 18-11-2024
    This method Save student information in CSV File
    Input : filpath - Its path where file is created
            L       - List of List which has student Information
    Output: None
'''

def save_to_csv(filepath, L):
    fw = open(filepath,"w", newline='')
    writer = csv.writer(fw)
    header = ["RNO","NAME","PER"]
    writer.writerow(header)

    for rec in L:
        writer.writerow(rec)
    fw.close()
    print(f"Data is Saved successfully in '{filepath}' ")

# L = [ [101,'AAA', 60],[102,'BBB', 70],[103,'CCC',80] ]

def save_to_sqldb(tablename, L ):
    con = get_mysqldb_connection()
    cur = con.cursor()

    #   rec ---> [102,'BBB', 70]
    for rec in L :
        try:
            cur.execute(f" insert into {tablename} values({rec[0]},'{rec[1]}',{rec[2]})")
        except:
            print("Rejected Record :", rec ) # Logs

    con.commit()
    print("All information is Saved in table :", tablename)

def save_to_mongodb(cname, L):
    collection = get_collection(cname)  # collection --> db.student

    for rec in L:
        d = {'rno': rec[0], 'name': rec[1], 'per': rec[2]}
        collection.insert_one(d)

    print("Information is Saved in Collection : " + cname)





