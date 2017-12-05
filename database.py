#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import sqlite3

class SQLite(object):
    """docstring for SQLite"""
    def __init__(self, dbPath):
        self.dbPath = dbPath
        self.adl = None
        self.cursor = None

    def connectToDB(self):
        try:
            self.adl = sqlite3.connect(self.dbPath)
            self.cursor = self.adl.cursor()
        except Exception as e:
            fo = open("log.txt", "a")
            fo.write( time.asctime(time.localtime(time.time())) + str(e) + '\n' )
            fo.close()
        
    def insert(self, dataID):
        try:
            self.cursor.execute("INSERT into dataids (dataID) values (%s)" % dataID)
        except Exception as e:
            fo = open("log.txt", "a")
            fo.write( time.asctime(time.localtime(time.time())) + str(e) + '\n' )
            fo.close()

    def select(self, dataID):
        try:
            select_result = self.cursor.execute("SELECT dataID from dataids where dataID='%s'" % dataID)
            select_result = list(select_result)
            if len(select_result) == 0:
                return False
            else:
                return True
        except Exception as e:
            fo = open("log.txt", "a")
            fo.write( time.asctime(time.localtime(time.time())) + str(e) + '\n' )
            fo.close()
            return False
