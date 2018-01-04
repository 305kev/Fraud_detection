"""
The online prediction engine
"""

from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from src.data_processing import DataProcessing
import json


def prediction(model, to_predict):
    """
    Uses a model to predict the probability of fraud for a single instance.
    :param model: object, a trained SK-Learn style model object
    :param to_predict: raw byte json from a URL query
    :return: df1: Dataframe, with the predicted probability added
    """
    df1 = decode_stream(to_predict)
    processed_example = DataProcessing(False, df1)
    processed_example.transform()
    x = processed_example.df
    Proba = model.predict_proba(x)[:, 1][0]
    ## Add one column to indicate the risk level
    if Proba > 0.5 and Proba  <= 0.8:
        df1["risk_level"] = "medium"
    elif Proba > 0.8:
        df1["risk_level"] = "high"
    else:
        df1["risk_level"] = "low"
    df1["predict"] = Proba
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

# def connect_db(dbname = "Fraud_prediction",
#                   tablename = "Fraud_prediction_table", host="", port= ""):
#    client = MongoClient()
#    return client
#
#
# if __name__ == "__main__":
#    import urllib2
#    from time import sleep
#    import pickle
#    from pymongo import MongoClient
#    """
#    Debugging script
#    """
#    by = urllib2.urlopen("http://galvanize-case-study-on-fraud.herokuapp.com/data_point").read()
#    df = decode_stream(by)
#
#    cols_dashboard = ["org_name", "name", "payee_name"]
#
#    with open("app/rf_test.pkl") as f:
#        model = pickle.load(f)
#    client = connect_db()
#    json_output = prediction(model, by)
#    print(json_output)
#
