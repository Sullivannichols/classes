#!/usr/bin/env python3

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

@app.route('/')
def homepage():
	return '<h1>CSC211 HW7: Flask Assignment</h1>'

@app.route('/list/<int:number>')
def list(number):
    list = range(0,number)
    return render_template('list.html', number=number, list=list) 

