#!/usr/bin/env python
import sqlite3
class db(object):
        def __init__(self,database,tablename,id,name,passwd,conn)
                self.database = database
                self.tablename = tablename
                self.id = id
                self.name = name
                self.passwd = passwd
                self.conn = conn
        def connect(self,database):
            conn = sqlite3.connect("%s", % database)
            return conn.cursor
        def create(self,cursor):
            cursor.execute('create table %s (%s varchar(20) primary key,%s varchar(20), %s varchar(100))',% (tablename,id,name,passwd))
            cursor.close()
            conn.commit()
            conn.close()
        def delete(self,cursor):
            cursor.execute('drop ')    
