#!/usr/bin/python3
# import sqlalchemy
import MySQLdb
import sys

if __name__ == '__main__':
    # Getting Info
    usr = sys.argv[1]
    psw = sys.argv[2]
    db = sys.argv[3]
    state = sys.argv[4]

    # Injection Prevention
    if "\"" in state:
        name = name.split("\"")[0]
    if "\'" in state:
        name = name.split("\'")[0]

    # Setting Up Connection - localhost and 3306 are default
    conn = MySQLdb.connect(
        host="localhost",
        user=usr,
        passwd=psw,
        db=db,
        port=3306)

    # finding the information
    db = conn.cursor()
    db.execute("SELECT cities.name FROM cities,\
    states WHERE states.id = cities.state_id AND\
    states.name = '{}' ORDER BY cities.id ASC;".format(state))

    # Grabbing the data
    query = db.fetchall()

    # printing info
    listOfStates = []
    for row in query:
        listOfStates += row

    for i in range(len(listOfStates)):
        if i < len(listOfStates) - 1:
            print(listOfStates[i], end=", ")
        else:
            print(listOfStates[i])

    # closing connection
    db.close()
    conn.close()
