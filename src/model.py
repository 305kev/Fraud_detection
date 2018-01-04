from src.data_processing import load_data, DataProcessing
from sklearn.ensemble import RandomForestClassifier
import pickle


def build_model(input_file, output_model):
    """
    Build the model from training data and save as a pkl file.
    The current model being used is a random forest classifier.
    :param input_file: Input jason file for raw data
    :param output_model: Output model in cPickle
    :return: Saved model to output_model
    """
    raw_data = load_data(input_file)
    pre_process_all = DataProcessing(True, raw_data)
    pre_process_all.transform()
    x_all = pre_process_all.df.drop(["fraud"], axis=1)
    y_all = pre_process_all.df["fraud"]
    best_rf = RandomForestClassifier(max_features=None, n_estimators=150, max_depth=30)
    best_rf.fit(x_all, y_all)
    with open(output_model, 'wb') as f:
        cPickle.dump(best_rf, f)


if __name__ == '__main__':
    """
    Debugging code for testing purposes
    """
    input_data = "data/data.json"
    output = "rf_test.pkl"
    build_model(input_data, output)
