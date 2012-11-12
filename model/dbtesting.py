#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys
import pickle
#http://stackoverflow.com/questions/5500332/cant-connect-the-postgresql-with-psycopg2
#http://rohitnair.info/installing-postgresql-on-os-x-lion/
#https://gist.github.com/1852087
#
#need to do this 
#sudo sysctl -w kern.sysv.shmall=65536
#sudo sysctl -w kern.sysv.shmmax=16777216 



def initDB():
    con = None
    con = psycopg2.connect(database='testingdb', host="/tmp/", user='colinwinslow') 
    cur = con.cursor()
    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, hash int, data varchar, frequency int);")
    con.commit()
    if con:
        con.close()
        
def addItem(hash,item):
    con = None
    con = psycopg2.connect(database='testingdb', host="/tmp/", user='colinwinslow') 
    cur = con.cursor()
    if not fetch(hash):
        cur.execute("INSERT INTO test (hash, data) VALUES (%s, %s)" , (hash, pickle.dumps(item)))
        con.commit()
        print "added"
    else: print "already there"
    if con: 
        con.close()
        
def fetch(hash):
    con = None
    con = psycopg2.connect(database='testingdb', host="/tmp/", user='colinwinslow') 
    cur = con.cursor()
    cur.execute('SELECT * FROM test WHERE hash = %s;', (str(hash),))
    return cur.fetchall()

