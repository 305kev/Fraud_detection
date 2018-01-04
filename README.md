# Fraud_detection

## Goal:
We received a data file of just over 14,000 records from a fundraising events hosting site.
Approximately 1900 of these events were marked as fraudulent. We were tasked with building a
prototype web app and machine learning model that would be able to dynamically alert the client
to transactions that appear to be fraudulent

## Instructions for use
First, build a model by calling model.py from the command line. This will create a pickle file for you
Once this is done, if desired, start running the app/live_predicting.py function from the command line. This will
start generating prediction examples for you.

More detailed instructions one running the app itself can be found in the app/README.md file.

## Features
All code for this section can be found in src/data_processing.py

### Defining the target
There were multiple types of fraud that were reported by the client. We created a target class
variable to assign all of these types to fraud, and the rest to non-fraud. Thus, we cast this as a
binary decision problem.

### Features and Feature Engineering
Following an exploratory data analysis, we decided to retain a number of fields for data analysis,
and to engineer features from other fields

The columns that we kept are:
- body_length
- channels
- delivery_method
- fb_published
- gts
- has analytics
- has_logo
- name_length
- num_order
- num_payouts
- org_twitter
- org_facebook
- sale_duration
- show_map
- user_age

We also engineered the following features that showed discrimination during exploratory data analysis:
-  A boolean indicating country codes with a high probability of fraudulent transactions
-  Booleans indicating high and medium risk email domains
-  A boolean indicating the gmail email domain
-  The number of previous payouts made to the organizer
-  Whether or not a venue country was specified

## Model building

Code for the model building procedure is found in src/model.py. When you run this code
from the command line, this will generate a pickle file in the data folder.

### Optimization Methodology:

We performed a train-test split, with the proportions at 80/20. A random forest
classifier was chosen for its good out of the box performance, and the model
parameters above were tuned using a grid search, with recall as the optimization
scoring metric.

The optimization was done using 5-fold cross-validation of the training set, with
an additional validation step performed afterwards on a hold-out data set. The results
are as follows:

### Model Performance
The model that we used was a random forest classifier, with the following parameters:
- n_estimators = 150
- man_depth = 30
- max_features = None

Cross-validated precision = 0.928
Cross-validated recall = 0.641

Validation set precision = 0.946
Validation set recall = 0.646

This model was created and save as a Pickle file for later predictive use.

With additional time, we would try out a wider range of models (for example
boosted decision trees, logistic regression, support vector machines) to see if
we could get an improved recall score. We would also make a more concerted effort to
produce a cost-benefit matrix, with which we could optimize the classification threshold.

## Fraud Detection Web App

### Online prediction

An online prediction engine is in src/predict.py, and prediction examples are obtained from
a remote server in the app/live_predicting.py file.

Running the live_predicting.py file will cause a new prediction example to be created every 30 seconds,
and stored in a MongoDB database. Every time that a new example is obtained, the predict.py file will run
a prediction using the model that was previously created. The results of the prediction, alongside all of
the raw information present will be stored in the Mongo database, for use in the web app's dashboard.

### App functionality

The app permits three possible actions:
- The ability to manually paste a json into a text box, and run a prediction using the json
- The ability to grab a single live prediction immediately, and see the result of the prediction on it
- The ability to extract the 10 most recent records from the database.

In all cases, the following information is displayed, to give the final investigator sufficient information
with which to pursue a possible fraud case:
- The name of the organizing non-profit
- The name of the event that was organized
- The name of the payee
- The risk of fraud.

Initially, we used the following criteria to assess the risk of fraud:
- High risk: probability > 0.8
- Medium risk: 0.5 < probability <= 0.8
- Low risk: probability <= 0.5
