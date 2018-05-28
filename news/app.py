#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from flask import Flask, abort, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# the  database's name is article
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/article'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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


@app.route('/')
def index():
    files = File.query.all()
    return render_template('index.html',files=files)

@app.route('/files/<file_id>')
def file(file_id):
    item=(File.query.filter_by(id=1).first())
    return render_template('file.html',item=item)

@app.route('/files/')
def files():
    return render_template('404.html')

if __name__ == '__main__':
    # TODO
    pass
