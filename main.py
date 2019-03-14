# -*- coding:utf-8 -*-
from sklearn.externals import joblib
from flask import Flask, jsonify, request
import pandas as pd
from sklearn import datasets
from flask_httpauth import HTTPBasicAuth # ←追記
import json
app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john": "hello",
    "susan": "bye"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/predict/<string:clf_file>', methods=['POST'])
@auth.login_required
def predict(clf_file):
    clf = joblib.load("{}.pkl".format(clf_file))
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return flask.jsonify(res='error'), 400
    data = request.json
    print(type(data))
    query = pd.io.json.json_normalize(data)
    print("check")
    cols = joblib.load("{}_cols.pkl".format(clf_file))
    query = query[cols]
    prediction = clf.predict(query)
    
    return jsonify({'prediction':prediction.tolist()})


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0')
