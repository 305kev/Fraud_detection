This folder contains the web application of the fraud prediciton model. We read data points lively from http://galvanize-case-study-on-fraud.herokuapp.com/data_point, which generate purchase record for prediction. 

The system requirement:
+ Python 2.7
+ Pymongo 3.4.0
+ flask 0.12.2
+ cPickle 1.71
+ urllib2 2.7


All the record is read and make fraud prediciton based on a Random Forest Model we trained on preprietary data sets from Galvanize. 
