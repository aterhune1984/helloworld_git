#!/usr/bin/env python

from flask import Flask, request, jsonify
import os

application = Flask(__name__)

@application.route('/')
def index():
    env = os.environ['ENVIRONMENT']
    return "updated Hello World from " + env

@application.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a',0,type=int)
    b = request.args.get('b',0,type=int)
    return jsonify(result=a + b)



if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0')

