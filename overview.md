The model that we used was a random forest classifier, with the following parameters:
- n_estimators = 150
- man_depth = 30
- max_features = None

We performed a train-test split, with the proportions at 80/20. A random forest
classifier was chosen for its good out of the box performance, and the model
parameters above were tuned using a grid search, with recall as the optimization
scoring metric.

The optimization was done using 5-fold cross-validation of the training set, with
an additional validation step performed afterwards on a hold-out data set. The results
are as follows:

Cross-validated precision = 0.928
Cross-validated recall = 0.641

Validaton set precision = 0.946
Validation set recall = 0.646

With additional time, we would try out a wider range of models (for example
boosted decision trees, logistic regression, support vector machines) to see if
we could get an improved recall score. We would also make a more concerted effort to
produce a cost-benefit matrix, with which we could optimize the classification threshold.
