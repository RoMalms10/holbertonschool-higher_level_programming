#!/usr/bin/python3
''' This module queries a TABLE and filters out information '''


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * \
                 FROM states \
                 WHERE name \
                 LIKE 'N%' \
                 ORDER BY id ASC")
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    db.close()
