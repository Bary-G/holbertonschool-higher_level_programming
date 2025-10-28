#!/usr/bin/python3
"""
Module: A Python script that lists all states from a MySQL database.
"""

import sys
import MySQLdb


def main():
    """Connect to MySQL and list all states in the database."""
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        db.close()
    except MySQLdb.Error as err:
        print("MySQL Error:", err)
        sys.exit(1)


if __name__ == "__main__":
    main()
