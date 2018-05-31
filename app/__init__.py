#! /bin/usr/python3 
# coding=utf-8

from flask import Flask

from .main import main

def create_app(config_name=''):
  app = Flask(__name__)

  app.register_blueprint(main)

  return app
