import mysql.connector

# MySQL Configuration Properties

HOSTNAME = "localhost"
PORT     = "3300"  # For Your machine 3306
USERNAME = "root"
PWD      = "root"
DB_NAME  = "py24db"
connection = None  # ref

def get_mysqldb_connection():
    global  connection
    if connection is None:
        connection = mysql.connector.connect(host=HOSTNAME, port=PORT, user= USERNAME, password= PWD, database= DB_NAME)
        print("MySQL is Connected !!!")
    return connection


def close_mysqldb_connection():
    global  connection
    if connection is not None:
        connection.close()
        connection = None
        print("MySQL is Dis-Connected !!!")




