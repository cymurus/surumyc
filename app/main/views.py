#! /bin/usr/python3 
# coding=utf-8

from flask import render_template, session, redirect, url_for, current_app, request
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
  request.headers
  # param_post=request.form['form_test']
  # request.args.get('test')
  return render_template('index.html', title='0')