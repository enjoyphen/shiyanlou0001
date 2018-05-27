#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import os
import json
from flask import Flask, abort, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# the  database's name is article
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/article'
db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<id:%s>'% self.id
class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    def __init__(self,title,created_time,category_id,content):
        self.title = title
        self.create_time = created_time
        self.category_id = category_id
        self.content= content
    def __repr__(self):
        return '<title:%s>'%self.title
db.create_all()
java = Category('Java')
python = Category('Python')
file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
file2 = File('Hello Python',datetime.utcnow(),python, 'File Content - Pythonis cool!')
db.session.add(java)
db.session.add(python)
db.session.add(file1)
db.session.add(file2)
db.session.commit()
print(java.id)
path0 = '/home/shiyanlou/files/'
files = (os.listdir(path0))
 
@app.route('/')
def index():
    str = []
    for file in files:
        with open(path0+file) as f:
            jsonfield = json.load(f)
            str.append(jsonfield['title'])
    return '{}\n{}'.format(str[0],str[1])

@app.route('/files/<filename>')
def file(filename):
    if os.path.isfile(path0+filename+'.json'):
        with open(path0+filename+'.json') as f:
            return f.read()
    else:
        return render_template('404.html')

@app.route('/files/')
def files():
    return render_template('404.html')

