from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sys import argv
from src.data_processing import DataProcessing
import json
import urllib2
from time import sleep
import cPickle as pickle
from pymongo import MongoClient

"""
The online prediction engine
"""

def prediction(model, to_predict):
    """
    Loads a pkl file containing the model to estimate the probability of fraud
    Loads the result into a mongoDB database
    :param model: object, a trained model object
    :param json_out: json code with the predicted probability added.
    """
    df1 = decode_stream(to_predict)
    processed_example = DataProcessing(False, df1)
    processed_example.fit()
    X = processed_example.df
    Proba = model.predict_proba(X)[:,1][0]
    ## Add one column to indicate the risk level
    if Proba > 0.5 and Proba  <= 0.8:
        df1["risk_level"] = "medium"
    elif Proba > 0.8:
        df1["risk_level"] = "high"
    else:
        df1["risk_level"] = "low"
    df1["predict"] = Proba
    print(type(df1["predict"]))
    return df1.T.to_dict().values()[0]


def decode_stream(stream):
    """
    Decodes json byte stream into a pandas dataframe
    :param stream: json byte stream of prediction instance
    :return: df: pandas dataframe containing prediction instance
    """
    stream = stream.decode()
    data = json.loads(stream)
    data["previous_payouts"] = [data["previous_payouts"]]
    data["ticket_types"] = [data["ticket_types"]]
    return pd.DataFrame(data)


def read_stream(sleepsec = 1):
    sleep(sleepsec)
    return urllib2.urlopen("http://galvanize-case-study-on-fraud.herokuapp.com/data_point").read()

def connect_db(dbname = "Fraud_prediction",
                   tablename = "Fraud_prediction_table", host="", port= ""):
    client = MongoClient()
    return client


if __name__ == "__main__":
   """
   Runs when the script is called from the command
   """
   by = urllib2.urlopen("http://galvanize-case-study-on-fraud.herokuapp.com/data_point").read()
   df = decode_stream(by)

   with open("rf_test.pkl") as f:
       model = pickle.load(f)
   client = connect_db()
   json_output = prediction(model, by)
   print(json_output)

