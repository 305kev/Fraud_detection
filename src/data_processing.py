"""
A set of functions that will process that data so that it can be used for model building.
"""

import pandas as pd

def load_data(filename):
    """
    Load the data in json format.
    :param filename: str, the relative path to a json file
    :return: df, a pandas dataframe of the json file
    """
    return pd.read_json(filename)


class DataProcessing():
    """
    A class that will handle all data preprocessing
    """
    def __init__(self, flag, df):
        """
        Instantiate the class.
        :param flag - Boolean, True indicates training data
        :param df - a pandas dataframe to be preprocessed
        """
        self.df = df
        self.train = flag


    def run_preprocessing(self):
        """
        Controls the preprocessing process
        """
        if self.flag
            self._add_target()


    def _convert_unix_to_datetime(self):
        """
        Convert all time columns from unix time to datetime.
        :param df: pandas dataframe of the fraud detection data
        :return: df2: pandas dataframe, with unix dates converted to datetimes
        """
        pass


    def _add_target(self):
        """
        Add class labels for the fraudulent transactions training data
        :param df: pandas dataframe
        :return: d
        """
        self.df["fraud"] = df["acct_type"].eq("premium").mul(1)



