import pymongo

from migration.migrate import csv_to_mongodb
from config.mongodb.configuration import get_collection

while True:
    print("1: CSV to MONGODB")
    print("2: CSV to SQLDB")
    print("3: EXIT")

    choice = int(input("What is your Choice : "))

    if choice == 1:
        filename = input("Enter the File name :")
        cname = input("Enter Collection : ")
        filepath = "resources/" + filename
        csv_to_mongodb(filepath, cname)

    elif choice==2:
        print("AUS")
    elif choice==3:
        # close connection
       exit(0)
    else:
        print("\n******** INVALID CHOIDE********\n")


print("Welcome to Data Migration App")

# Migration Test Cases : CSV to SQLDB & MongoDB
# csv_to_sqldb(FILENAME, "student")
# csv_to_mongodb(FILENAME, "student")

#----------------------------------------------

# Migration Test Cases : SQLDB to CSV & MongoDB

# sqldb_to_csv("student", FILENAME)
# sqldb_to_mongodb("student", "student")

#----------------------------------------------
# Migration Test Cases : MongoDB to CSV & SQLDB

# mongodb_to_csv("student", FILENAME)
# mongodb_to_sqldb("student", "student")

#----------------------------------------------
# Migration Test Cases : User Input to CSV, MongoDB & SQLDB
#  n = int(input("How many Records : "))
# user_input_to_csv(n, FILENAME)
# user_input_to_sqldb(n, "student")
# user_input_to_mongodb(n, "student")

print("Byeee")

close_mysqldb_connection()
close_mongodb_connection()


'''

# Test Code save_to_csv()
L = [ [101,'AAA', 60],[102,'BBB', 70],[103,'CCC',80] ]
save_to_csv(FILENAME, L)

# Test Code for load_from_csv()
L = load_from_csv(FILENAME)
display_student_information(L)

# Test Code for save_to_sqldb
L = [ [101,'PPP', 60],[104,'QQQ', 70],[102,'SSS', 90],[105,'RRR',80] ]
save_to_sqldb("student", L)
'''