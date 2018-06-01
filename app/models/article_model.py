#! /bin/usr/python3 
# coding=utf-8

from datetime import datetime
import uuid

from .. import db

class Article(object):

  def __init__(self, title, content):
    self.title = title
    self.content = content
    self.post_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    self.mod_time = post_time
    self.vp = 0

  def save(self):
    sql = ' insert into article(id, title, content, post_time, mod_time, vp) values (?, ?, ?, ?, ?, ?); '
    params = (uuid.uuid1(), self.title, self.content, self.post_time, self.mod_time, self.vp)
    