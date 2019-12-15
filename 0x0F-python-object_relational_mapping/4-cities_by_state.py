#!/usr/bin/python3
# import sqlalchemy
import MySQLdb
import sys

if __name__ == '__main__':
    # Getting Info
    usr = sys.argv[1]
    psw = sys.argv[2]
    db = sys.argv[3]
    # name = sys.argv[4]

    # Injection Prevention
    # if "\"" in name:
    #     name = name.split("\"")[0]
    # if "\'" in name:
    #     name = name.split("\'")[0]

    # Setting Up Connection - localhost and 3306 are default
    conn = MySQLdb.connect(
        host="localhost",
        user=usr,
        passwd=psw,
        db=db,
        port=3306)

    # finding the information
    db = conn.cursor()
    db.execute("SELECT cities.id, cities.name, states.name FROM cities, states WHERE cities.state_id = states.id ORDER BY id ASC")

    # Grabbing the data
    query = db.fetchall()

    # printing info
    for row in query:
        print(row)

    # closing connection
    db.close()
    conn.close()
