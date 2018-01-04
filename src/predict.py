import cPickle as pickle
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sys import argv
from src.data_processing import DataProcessing
from src.database import mongobd_insert
from pymongo import MongoClient

"""
The online prediction engine
"""

def prediction(model, to_predict):
    """
    Loads a pkl file containing the model to estimate the probability of fraud
    Loads the result into a mongoDB database
    :param pklfile: str, the location of the pickled model
    :param to_predict: dataframe containing the instance to make a prediction about
    """


    processed_example = DataProcessing(False, to_predict)
    processed_example.fit()
    X = processed_example.df
    return model.predict_proba(X)[:,1]


if __name__ == "__main__":
    """
    Runs when the script is called from the command
    """
    file = argv[1]
    df1 = pd.read_json(argv[2])
    prob = prediction(file, df1)
    df1["predict"] = prediction(file, df1)
    json_inp = df1.T.to_dict().values()

    mongobd_insert(json_inp[0], tablename = "test")
    client = MongoClient()
    dbname = "Fraud_prediction"
    tablename = "test"
    db = client[dbname]
    table = db[tablename]
    print(table.find_one())