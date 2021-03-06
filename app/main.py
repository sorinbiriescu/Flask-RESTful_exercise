#!/usr/bin/env python3
"""
Documentation

See also https://www.python-boilerplate.com/flask
"""
import os

from flask import Flask, jsonify
from flask_cors import CORS
from logzero import logger
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('development.py')
    db.init_app(app)

    # Setup cors headers to allow all domains
    # https://flask-cors.readthedocs.io/en/latest/
    CORS(app)

    # Definition of the routes. Put them into their own file. See also
    # Flask Blueprints: http://flask.pocoo.org/docs/latest/blueprints

    from app.views import main_routes
    from app.api.resources import api_bp

    app.register_blueprint(main_routes)
    app.register_blueprint(api_bp)

    from app.api.resources import api,MessageItem, MessageList
    api.add_resource(MessageList, '/message','/message/', endpoint="message_list")
    api.add_resource(MessageItem, '/message/<int:id>', endpoint="message")

    return app

