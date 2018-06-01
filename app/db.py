#! /bin/usr/python3 
# coding=utf-8

import sqlite3

class DbConn(object):

  def __init__(self, db_name='surumyc_blog.db'):
    self.conn = sqlite3.connect(db_name)

  def exec(self, sql, params):
    cursor = self.conn.cursor()
    cursor.execute(sql, tuple(params))
    cursor.close()
    conn.commit()