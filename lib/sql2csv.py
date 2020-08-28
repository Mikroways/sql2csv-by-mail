#!/usr/bin/env python3
import mysql.connector, sys, os, csv


if __name__ == '__main__':
    try:
        query = sys.argv[1]
    except IndexError as e:
        sys.exit('Must send a SQL query')

if not os.getenv('DB_HOST') or \
    not os.getenv('DB_USER') or not os.getenv('DB_NAME'):
    sys.exit('Must set DB_HOST and DB_USER and DB_NAME')

connection = mysql.connector.connect(host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    db=os.getenv('DB_NAME'))

cur=connection.cursor()

cur.execute(query)
rows=cur.fetchall()
column_names = [i[0] for i in cur.description]
fp = sys.stdout
myFile = csv.writer(fp, lineterminator = '\n')
myFile.writerow(column_names)
myFile.writerows(rows)
fp.close()

cur.close()
connection.close()


