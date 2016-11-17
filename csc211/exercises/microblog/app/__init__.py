#!/usr/bin/env python3

from flask import Flask
from flask.ext.sqlalchemy import SQAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQAlchemy(app)

from app import views, models
