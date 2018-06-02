#! /bin/usr/python3 
# coding=utf-8

from flask import render_template, session, redirect, url_for, current_app, request
from . import main
from ..models import *

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
  article = {
    'title': 'Lorem ipsum dolor sit amet',
    # 'title': '蟑螂，杂草，梦想家',
    'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?Lorem ipsum dolor sit amet, consectetur adipisicing elit. Unde odio, inventore earum vel odit rem aliquam minus officia iusto. Ab maxime quis voluptatem soluta, reprehenderit quae possimus, perspiciatis necessitatibus ullam?',
#     'content': '''在黑暗中解一个绳结。我知道哪里有线，但不敢轻举妄动，因为我不知道哪根线会扯上长度未知的、足够消磨完我生命的灾难。
# 但很可笑，我还是随便扯了一根。因为在黑暗中，选哪一根并没有区别。

# 在走投无路时，选择的本身不重要，重要的是我们要能承受选择的结果。
# 或者你可以一直僵在黑暗中，拿着那个绳结，等太阳和你和线，一起枯萎。
# 又或者你敲碎了自己的脑门，迸出了光，来让你继续解这个绳结。
# 蟑螂，杂草，梦想家。



# 我没有开灯，继续胡乱解着耳机，困了。
# 困了的梦想家，只是一只蟑螂罢了。''',
    'post_time': '2018-05-29 21:53:13',
    'mod_time': '2018-06-01 18:00:21',
    'vp': 1,
  }
  return render_template('article_details.html', title=article['title'], article=article)

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
