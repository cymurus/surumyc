#! /bin/usr/python3 
# coding=utf-8

from flask import Flask

from .main import main
from .config import config

def create_app():
  app = Flask(__name__)

  config(app)

  app.register_blueprint(main)

  return app
