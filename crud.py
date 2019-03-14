# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth # ←追記

app = Flask(__name__)
auth = HTTPBasicAuth() # ←追記

users = { # ←追記
    "john": "hello", # ←追記
    "susan": "bye" # ←追記
} # ←追記

@auth.get_password # ←追記
def get_pw(username): # ←追記
    if username in users: # ←追記
        return users.get(username) # ←追記
    return None # ←追記

languages = [{'name' : 'java'}, {'name' : 'php'}, {'name' : 'ruby'}]

@app.route("/", methods = ['GET'])
@auth.login_required # ←追記
def test():
    return jsonify({'message' : "Hello, %s!" % auth.username()})

@app.route("/lang", methods = ['GET'])
@auth.login_required # ←追記
def returnAll():
    return jsonify({'langages' : languages})

@app.route("/lang/<string:name>", methods = ['GET'])
@auth.login_required # ←追記
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'langages' : langs[0]})

@app.route("/lang", methods = ['POST'])
@auth.login_required # ←追記
def addOne():
    language = {'name' : request.json['name']}
    languages.append(language)
    return jsonify({'langages' : languages})

@app.route("/lang/<string:name>", methods = ['PUT'])
@auth.login_required # ←追記
def editOne(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'langages' : langs[0]})

@app.route("/lang/<string:name>", methods = ['DELETE'])
@auth.login_required # ←追記
def removeOne(name):
    langs = [language for language in languages if language['name'] == name]
    languages.remove(langs[0])
    return jsonify({'langages' : languages})

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=3000)
