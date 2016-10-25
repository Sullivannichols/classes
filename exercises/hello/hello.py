#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD']=True

@app.route('/')
def hello_world():
	return 'Hello world!'

@app.route('/test')
def test_function():
	return '<h1>This is a test.</h1>'

@app.route('/test/<int:number>')
def test_function2(number):
	content = '<h1>Different more text for #{}</h1>'
	content = content.format(number)
	return content

#@app.route('/login', methods=['GET','POST'])
#def login():
#	if request.method == 'POST'
#		return 'This is a post'
#	else:
#		return 'This is a get'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
