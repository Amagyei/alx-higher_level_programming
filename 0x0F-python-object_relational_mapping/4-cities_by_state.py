#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv
if __name__ == '__main__':
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset='utf8')
    cur = conn.cursor()
    try:
        stmt = """
        SELECT cities.id, cities.name, states.name
        FROM cities, states
        WHERE cities.state_id = states.id
        ORDER BY cities.id ASC
        """
        cur.execute(stmt)
        rtn = cur.fetchall()
    except MySQLdb.Error:
        try:
            rtn = ("MySQLdb Error")
        except p:
            rtn = ("MySQLdb Error - IndexError")
    for i in rtn:
        print(i)
    cur.close()
    conn.close()
