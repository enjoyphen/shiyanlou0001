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
    category = db.relationship('Category',backref='cname')
    content = db.Column(db.Text)
    def __init__(self,title,created_time,category,content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content= content
    def __repr__(self):
        return '<title:%s>'%self.title
path0 = '/home/shiyanlou/files/'
files = (os.listdir(path0))
 
@app.route('/')
def index():
    str = File.query.all()
    str1 = str.cname
    return rendjer_template('index.html',str)

@app.route('/files/<file_id>')
def file(file_id):
    item = File.query.filter(id==file_id).first()
        return render_template('file.html',item)
    else:
        return render_template('404.html')

@app.route('/files/')
def files():
    return render_template('404.html')

