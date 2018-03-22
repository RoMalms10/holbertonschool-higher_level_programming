#!/usr/bin/python3
''' This module runs a query on a database to find states '''


if __name__ == "__main__":
    import MySQLdb
    from sys import argv


    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_db = cur.fetchall()
    for row in query_db:
        print(row)
    cur.close()
    db.close()
