#!/usr/bin/env python3

from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

@app.route('/')
def homepage():
	return '<h1>CSC211 HW7: Flask Assignment</h1>'

@app.route('/list/')
def list_home():
    return render_template('listform.html')

@app.route('/list/numbers', methods = ['POST'])
def list_render():
    number = int(request.form['number'])
    list = range(0,number)
    return render_template('list.html', number=number, list=list) 

