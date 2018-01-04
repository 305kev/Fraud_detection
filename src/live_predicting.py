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

def read_stream(sleepsec = 2):
    sleep(sleepsec)
    return urllib2.urlopen("http://galvanize-case-study-on-fraud.herokuapp.com/data_point").read()

def connect_db(dbname = "Fraud_prediction",
                   tablename = "Fraud_prediction_table", host="", port= ""):
    client = MongoClient()
    return client

def predict_to_database():
    json_inp = read_stream(45)
    json_output = prediction(model, json_inp)
    mongobd_insert(json_output, client, tablename=tablename)

if __name__ == '__main__':
    with open("../rf_test.pkl") as f:
        model = pickle.load(f)
    client = connect_db()
    dbname = "Fraud_prediction"
    tablename = "test4"
    predict_to_database()