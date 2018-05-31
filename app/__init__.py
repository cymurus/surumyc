#! /bin/usr/python3 
# coding=utf-8

from flask import Flask
# from flask_bootstrap import Bootstrap
# from flask_mail import Mail
# from flask_sqlalchemy import SQLAlchemy
# from config import config

# bootstrap = Bootstrap()
# mail = Mail()
# db = SQLAlchemy()

from .main import main

def create_app(config_name=''):
  app = Flask(__name__)
  # app.config.from_object(config[config_name])
  # config[config_name].init_app(app)

  # bootstrap.init_app(app)
  # mail.init_app(app)
  # db.init_app(app)

  app.register_blueprint(main)

  return app