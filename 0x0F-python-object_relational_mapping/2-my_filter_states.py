#!/usr/bin/python3
''' This module queries a TABLE and filters out information based on input'''


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * \
                 FROM states \
                 WHERE name \
                 LIKE '{}' \
                 ORDER BY id ASC".format(argv[4]))
    query = cur.fetchall()
    for row in query:
        if (row[1] == argv[4]):
            print(row)
    cur.close()
    db.close()
