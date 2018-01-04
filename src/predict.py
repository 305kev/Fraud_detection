from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sys import argv
from src.data_processing import DataProcessing
import json


"""
The online prediction engine
"""

def prediction(model, to_predict):
    """
    Loads a pkl file containing the model to estimate the probability of fraud
    Loads the result into a mongoDB database
    :param model: object, a trained model object
    :param to_predict: bytes object containing the instance to make a prediction about
    """
    df1 = decode_stream(to_predict)
    processed_example = DataProcessing(False, df1)
    processed_example.fit()
    X = processed_example.df
    return model.predict_proba(X)[:,1]


def decode_stream(stream):
    """
    Decodes json byte stream into a pandas dataframe
    :param stream: json byte stream of prediction instance
    :return: df: pandas dataframe containing prediction instance
    """
    stream = stream.decode().replace("'", '"')
    data = json.loads(stream)
    data["previous_payouts"] = [data["previous_payouts"]]
    return pd.DataFrame(data)


#if __name__ == "__main__":
#    """
#    Runs when the script is called from the command
#    """
#    file = argv[1]
#    df1 = pd.read_json(argv[2])
#    prob = prediction(file, df1)
#    print(prob)