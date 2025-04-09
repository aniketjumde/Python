import csv

from config.mongodb.configuration import get_collection
from config.mysqldb import get_mysqldb_connection
from myio.myinput import get_rno, get_name, get_per


def load_from_csv(filepath):
    fr = open(filepath, "r")
    reader = csv.reader(fr)
    L = list(reader)  # list() method reads from reader object which is pointing to student.csvs and returns List-of-List
    del L[0]          # Here I am deleting Header Row ["RNO","NAME", "PER"]
    fr.close()
    return L

# Preparing List of list student records from user
def load_from_user(n): # n: 3
    L = []  #[[101,AAA,60]]

    for i in range(n):
        rno  = get_rno()
        name = get_name()
        per  = get_per()
        TL = [rno,name,per]  # packing of List TL=[102,BBB,70]
        L.append(TL)
    return L


def load_from_sqldb(tablename):
    con = get_mysqldb_connection()
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {tablename}")

    return [ list(T)  for T in cur.fetchall()  ]

'''
    data = cur.fetchall()  # data : [ (101,'AAA', 60) , (102,'BBB', 70) ]

    L = [ list(T)  for T in data ]
    return L
'''
    # L = [] # L --> [ [101,AAA,60] , [102,BBB,70] ]
    #
    # for rec in data:
    #
    #     TL = [ rec[0], rec[1], rec[2] ]   # Packing to List [102,BBB,70]
    #     L.append(TL)

def load_from_mongodb(cname):
    collection =  get_collection(cname)  # collection ---> db.student
    L = []

    result = collection.find({},{ '_id' : 0})

    # d---> {rno: 104, name: 'DDD', city: 'Sangvi'},

    for d in result :
        try:
            TL = [ d['rno'],  d['name'], d['per']]     # TL --> [101,AAA,60]
            L.append(TL)
        except:
            print("Rejected Record : ", d)

    return  L











