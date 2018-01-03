# Case study project scope

The purpose of this document is to provide a definition of the project scope and requirements.

The columns that we intend to keep to use for prediction are:
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



The following engineered features will also be used:
- Boolean list of countries with high fraud rates fraud_country
- high_risk, medium_risk and gmail email domain Booleans
- number of previous payouts



Things we would like to look at in the future:
- Difference between event created and event published
- Difference between payout date and event published/created
- sale duration - sale_duration2 or boolean if they are different
- user_type (as dummies)

In the first instance, we will try to run and build a simple random forest classifier.
This should provide us with a sufficiently simple model, that can quickly run in an
online environment to power a prediction engine.

In this case, a low number of false positives and a low number of false negatives
are required. Thus in the first instance, we will utilize accuracy as a metric. If
time allows, we will attempt to define a cost-benefit matrix with which to better
optimize the model.
