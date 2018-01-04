import cPickle as pickle
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sys import argv
from src.data_processing import DataProcessing


"""
The online prediction engine
"""

def prediction(pklfile, to_predict):
    """
    Loads a pkl file containing the model to estimate the probability of fraud
    Loads the result into a mongoDB database
    :param pklfile: str, the location of the pickled model
    :param to_predict: dataframe containing the instance to make a prediction about
    """

    with open(pklfile, "rb") as f:
        model = pickle.load(f)

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
    print(prob)