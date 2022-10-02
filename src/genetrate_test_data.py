
# a simple script o generate test data in MySQL

import uuid
import random
import string
import sys
import time
import mysql.connector

# print the current timestamp

count = 3
if len(sys.argv) > 1:
  count = int(sys.argv[1])

mydb = mysql.connector.connect(host="localhost", user="root",password="test1", database="benchmark1")


mycursor = mydb.cursor()

for i in range(0, count):
  # make a random UUID, random int and random string. 
  one_uid = uuid.uuid4()
  one_int =  random.randint(0, 1000000000)
  one_string = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=30))

  sql = "INSERT INTO test1(ruuid, rint, description) values('%s', %s, '%s') ; "%(one_uid, one_int, one_string)
  print(sql)
  ts_startsql = round(time.time() *1000)
  mycursor.execute(sql)

  mydb.commit()
  ts_endsql = round(time.time() *1000)
  print(ts_endsql - ts_startsql)

