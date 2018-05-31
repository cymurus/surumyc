#! /bin/usr/python3 
# coding=utf-8

from app import create_app
# from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand

app = create_app('config')
# manager = Manager(app)
# migrate = Migrate(app, db)

# manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  app.run(debug=True)