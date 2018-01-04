from flask import Flask
from flask import render_template, request
import cPickle as pickle
from sklearn.ensemble import RandomForestClassifier
import urllib2
from pymongo import MongoClient
from time import sleep
import numpy as np
import pandas as pd
from src.predict import prediction
from src.database import mongobd_insert


app = Flask(__name__)


def read_stream(sleepsec = 1):
    sleep(sleepsec)
    return urllib2.urlopen("http://galvanize-case-study-on-fraud.herokuapp.com/data_point").read()

def connect_db(dbname = "Fraud_prediction",
                   tablename = "Fraud_prediction_table", host="", port= ""):
    client = MongoClient()
    return client

def tem_read():
    df1 = pd.read_json("../data/example.json")
    return df1


@app.route('/')
def index():
    return render_template('index.html', title='Fraud Prediction', data=None)


@app.route('/get', methods = ["GET"])
def get_entry():
    return render_template('index.html', title='Fraud Prediction', data=None)

@app.route('/score', methods=['POST'])
def score():
    #doc = request.form['text1']
    #model_select = request.form["model_selected"]
    # if isinstance(doc, basestring):
    #     doc = [doc]
    # sec_name = model_c.predict(doc)
    json_inp = read_stream()
    json_output = prediction(model, json_inp)
    mongobd_insert(json_output, client)
    return render_template('index.html', title='make prediction', data=zip([],[],[]))

if __name__ == '__main__':
    with open("../rf_test.pkl") as f:
        model = pickle.load(f)
    client = connect_db()
    app.run(host='0.0.0.0', port=8080, debug=True)
