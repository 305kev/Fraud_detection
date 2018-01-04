from src.data_processing import load_data, DataProcessing
from sklearn.ensemble import RandomForestClassifier
import cPickle


def build_model(input_file, output_model, model_name = "RandomForestClassifier"):
    '''
    :param input_file: Input jason file for raw data
    :param output_model: Output model in cPickle
    :param model_name: "RandomForestClassifier was selected and optimized Model_buiding.ipynb"
    :return: Saved model to output_model
    '''
    raw_data = load_data(input_file)
    pre_process_all = DataProcessing(True, raw_data)
    pre_process_all.fit()
    X_all = pre_process_all.df.drop(["fraud"], axis=1)
    y_all = pre_process_all.df["fraud"]
    best_rf = RandomForestClassifier(max_features=None, n_estimators=150, max_depth=30)
    best_rf.fit(X_all, y_all)
    with open(output_model, 'wb') as f:
        cPickle.dump(best_rf, f)

if __name__ == '__main__':
    input_file = "data/data.json"
    output_model = "rf_test.pkl"
    build_model(input_file, output_model)