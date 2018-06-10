#! /bin/usr/python3 
# coding=utf-8

import os
import uuid
import json

db_root = 'databases'

class BaseModel(object):

  '''
    split_list: ['content']
    then data['content'] will be saved in the file "uuid.content"
  '''
  def __init__(self, model, split_list=[]):
    self.db_path = '/'.join([db_root, model])
    if not os.path.exists(self.db_path):
      os.makedirs(self.db_path)
    self.split_list = split_list      

  def _write(self, filename, data, mode='w'):
    filepath = '/'.join([self.db_path, filename])
    if not os.path.exists(filepath):
      os.makedirs(filepath)
    # path not exist
    f = open(filepath, mode)
    f.write(data)
    f.close()

  def _read(self, filename, mode='r'):
    filepath = '/'.join([self.db_path, filename])
    if not os.path.exists(filepath):
      return None
    f = open(filepath, mode)
    data = f.read()
    f.close()
    return date

  def _rm(self, filename):
    filepath = '/'.join([self.db_path, filename])
    if not os.path.exists(uuid):
      return 404
    # path not exist
    try:
      os.remove(filepath)
    except Exception as e:
      return 500
    return 200

'''
  data is like {
    'title': 'Lorem ipsum',
    'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam'，
    'info': {
      'post_time': '19991203',
      'mod_time': '19991203',
      'vp': '0',
    }
  }
  根据 split_list 将 content 和其他信息分开存
'''
  def db_save(self, data):
    data = json.loads(data)
    if 'uuid' in data:
      elem_id = data['uuid']
      del data['uuid']
    else:
      elem_id = uuid.uuid1()

    for part in self.split_list:
      self._write(sp_filename + '.' + part, data[part])
      del data[part]

    data = json.dumps(data)
    self._write(elem_id, data)

    return 0


  def db_get(self, uuid, sp_list=[]):
    


  def db_update(self, data):
    self.db_save(data)


  def db_delete(self, uuid):
    files_to_delete = [uuid + '.' + part for part in self.split_list]
    files_to_delete.append(uuid)
    for file in files_to_delete:
      self._rm(file)
