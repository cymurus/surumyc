#! /bin/usr/python3 
# coding=utf-8

from flask import render_template, session, redirect, url_for, current_app, request
from . import main

'''
*********   Page routing   **********
'''

@main.route('/', methods=['GET'])
def index():
  request.headers
  # param_post=request.form['form_test']
  # request.args.get('test')
  return render_template('index.html', title='0')

@main.route('/article', methods=['GET'])
def list_article():
  # get articles
  articles = []
  return render_template('article.html', title='article', articles=articles)

@main.route('/article/<string:article_id>', methods=['GET'])
def list_article_details(article_id):
  # get articles
  article_name = article_id
  article = {
    'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?'
  }
  return render_template('article_details.html', title=article_name, article=article)

@main.route('/picture', methods=['GET'])
def list_picture():
  # get pictures
  pictures = []
  return render_template('picture.html', title='gallery', pictures=pictures)

@main.route('/message', methods=['GET'])
def list_message():
  # get messages
  messages = []
  return render_template('message.html', title='board', messages=messages)

@main.route('/about', methods=['GET'])
def about_info():
  # get messages
  return render_template('about.html', title='cymurus.')


'''
*********   Update routing   **********
'''

# ---------- article ------------

@main.route('/article', methods=['POST'])
def post_article():
  # TO-DO add
  article_id = '1'
  url_redirect_to = '/article/%s' % article_id
  return redirect(url_redirect_to)

@main.route('/article', methods=['DELETE'])
def delete_article():
  # TO-DO delete
  url_redirect_to = '/article'
  return redirect(url_redirect_to)

@main.route('/article/<string:article_id>', methods=['PUT'])
def update_article(article_id):
  # TO-DO update
  url_redirect_to = '/article/%s' % article_id
  return redirect(url_redirect_to)



# ---------- message ------------

@main.route('/message', methods=['POST'])
def post_message():
  # TO-DO add
  url_redirect_to = '/message'
  return redirect(url_redirect_to)

@main.route('/message', methods=['DELETE'])
def delete_message():
  # TO-DO delete
  url_redirect_to = '/message'
  return redirect(url_redirect_to)



# ---------- picture ------------

@main.route('/picture', methods=['POST'])
def post_picture():
  # TO-DO add
  url_redirect_to = '/picture'
  return redirect(url_redirect_to)

@main.route('/picture', methods=['DELETE'])
def delete_picture():
  # TO-DO delete
  url_redirect_to = '/picture'
  return redirect(url_redirect_to)
