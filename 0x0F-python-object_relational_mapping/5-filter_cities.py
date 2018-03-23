#!/usr/bin/python3
''' This module queries cities TABLE and joins it with states
    and sorts by input
'''


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name \
                 FROM cities \
                 INNER JOIN states \
                 ON cities.state_id = states.id \
                 WHERE states.name=%s \
                 ORDER BY cities.id ASC", (argv[4], ))
    query = cur.fetchall()
    for row in range(len(query) - 1):
        print(query[row][0], end=", ")
    print(query[row + 1][0])
    cur.close()
    db.close()
