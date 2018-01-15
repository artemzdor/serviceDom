#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, session, redirect, url_for, escape, request, jsonify

app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello():
    str = '''
    <html>
      <head>
        <title>Home Page</title>
      </head>
      <body>
        <h3>Привет Макс это наш сервис!!!</h3>
      </body>
    </html>
    '''
    return str


if __name__ == "__main__":
    app.run(debug=True)