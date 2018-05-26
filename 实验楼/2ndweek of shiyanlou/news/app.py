#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import os
import json
from flask import Flask, abort, render_template

app = Flask(__name__)

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

