#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from flask import Flask, abort, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pymongo import MongoClient


app = Flask(__name__)
# the  database's name is article
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/article'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
client = MongoClient('127.0.0.1',27017)
# the mongodb name is 'shi'
mdb = client.shi 


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
     # tag list
      def _gettags(self):
          try:
<<<<<<< HEAD
             lst= mdb.user.find_one({'name':self.id})
             if lst is None:
                 mdb.user.insert_one({'name':self.id, 'tags':[]})
                 lst = []
=======
             lst= mdb.user.find_one({'name':self.id}) # logical is wrong
             if lst is None: # though lst is not None, lst['tags'] may be None 
                 mdb.user.insert_one({'name':self.id, 'tags':[]})
                 lst = [] 
>>>>>>> 2e6ae2705a648ad35e93769c16e33aa6b3b6cfb1
         except KeyError:
             mdb.user.update_one({'name':self.id,'tags':[]})
             lst = []
         return lst
    @property
    def tags(self):
        return self._gettags() 
    # add a tag to article
    def add_tag(self, tag_name):
    # add a tag named by tag_name and save it to mdb
    # add tag_name to dict
        lst_tags = self._gettags()
        if tag_name not in lst_tags:
            mdb.user.update_one({'name':self.id},
                {'$set':{'tags':lst_tags.append(tag_name)}})
        else:
            return None
    # remove the tag
    def remove_tag(self, tag_name):
        # remove the tag from current artilce in mdb
        lst_tags = self._gettags()
        if tag_name in lst_tags:
            mdb.user.update_one({'name':self.id},
                {'$set':{'tags':lst_tags.remove(tag_name)}})
        else:
            return None

db.create_all()
java = Category('Java')
python = Category('Python')
file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is     cool!')
file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Pyth    on is cool!')
db.session.add(java)
db.session.add(python)
db.session.add(file1)
db.session.add(file2)
db.session.commit()
file1.add_tag('tech')
file1.add_tag('java')
file1.add_tag('linux')
file2.add_tag('tech')



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
