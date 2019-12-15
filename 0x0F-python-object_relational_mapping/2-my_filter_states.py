#!/usr/bin/python3
# import sqlalchemy
import MySQLdb
import sys

if __name__ == '__main__':
    # Getting Info
    usr = sys.argv[1]
    psw = sys.argv[2]
    db = sys.argv[3]
    name = sys.argv[4]

    # Setting Up Connection - localhost and 3306 are default
    conn = MySQLdb.connect(
        host="localhost",
        user=usr,
        passwd=psw,
        db=db,
        port=3306)

    # finding the information
    db = conn.cursor()
    db.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(name))

    # Grabbing the data
    query = db.fetchall()

    # printing info
    for row in query:
        if row[1] == name:
            print(row)

    # closing connection
    db.close()
    conn.close()
