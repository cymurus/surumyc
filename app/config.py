#! /bin/usr/python3 
# coding=utf-8

def config(app):
  app.config['UPLOAD_FOLDER'] = 'static/uploads/'  
  app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif', 'ycf'])