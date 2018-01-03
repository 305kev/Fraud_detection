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


def convert_unix_to_datetime(df):
    """
    Convert all time columns from unix time to datetime.
    :param df: pandas dataframe of the fraud detection data
    :return: df2: pandas dataframe, with unix dates converted to datetimes
    """
    pass


