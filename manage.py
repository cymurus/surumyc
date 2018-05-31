#! /bin/usr/python3 
# coding=utf-8

from app import create_app

app = create_app('config')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8023, debug=True)
