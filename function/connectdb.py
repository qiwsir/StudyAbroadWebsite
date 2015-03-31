#!/usr/bin/env python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#connect database

import MySQLdb

conn = MySqldb.connect(host="localhost", user="root", passwd="123123", db="studyabroad", port=3036, charset="utf8")

cur = conn.cursor()


