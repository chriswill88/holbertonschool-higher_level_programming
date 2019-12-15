#!/usr/bin/python3
# import sqlalchemy
import MySQLdb
import sys

if __name__ == '__main__':
    # Getting Info
    username = sys.argv[1]
    dbpsw = sys.argv[2]
    dbname = sys.argv[3]

    # Setting Up Connection
    conn = MySQLdb.connect(host="localhost", user=username, passwd=dbpsw, db=dbname, port=3306)

    # finding the information
    db = conn.cursor()
    db.execute("SELECT * FROM states ORDER BY id ASC")

    # Grabbing the data
    query = db.fetchall()

    # printing info
    for row in query:
        print(row)

    # closing connection
    db.close()
    conn.close()
