Predicting if a person has diabete based on his health indicators
================
2022/11/23 (updated: 2022-11-25)

-   <a href="#summary" id="toc-summary">Summary</a>
-   <a href="#introduction" id="toc-introduction">Introduction</a>
-   <a href="#methods" id="toc-methods">Methods</a>
    -   <a href="#data" id="toc-data">Data</a>
    -   <a href="#analysis" id="toc-analysis">Analysis</a>
-   <a href="#results-and-discussion"
    id="toc-results-and-discussion">Results and Discussion</a>
-   <a href="#references" id="toc-references">References</a>

# Summary

To answer to the study question which is “Given a person’s health
indicators, can we know if he/she has diabete or not?”, we have split
the data into test and train and perfomed a transformation only on
numeric features. We have thereafter attempted to build different
classification models using Dummy Classifier, Decision Tree Classifier,
K-Neighbors Classifier, SVC and Logistic Regression. After looking at
cross-validations from the different models, the SVM and the Logistic
Regression models had high recall and f1 scores. The two models were
tuned and used on the test data. The f1 score for the tuned SVC was 0.38
as opposed to 0.391 for the tuned logistic regression. When it comes to
the recall scores, the SVC performed 0.792 as opposed to 0.792 for the
logistic regression. The two models are spotting a high proportion of
actual positives which is in our case people with diabete.

# Introduction

Diabete is a disease which affects many people around the world. This
disease is the result of the lack of insulin in the body. Insulin is a
hormone produced by your pancreas whose role is to regulate the amount
of glucose in the blood. Blood sugar must be carefully regulated to
ensure that the body functions properly. Too much blood sugar can damage
some organs, like blood vessels and nerves. Our body also needs insulin
in order to use sugar for energy. According to the International
Diabetes Federation “In 2021, Approximately 537 million adults (20-79
years) are living with diabetes. The total number of people living with
diabetes is projected to rise to 643 million by 2030 and 783 million by
2045”. With these alarming figures, many experts claim that it is
important to have a good lifestyle, i.g. physical activity and good
eating habits, in order to avoid this disease or avoid its complicated
form. Can we really tell if a person is suffering from diabetes or not,
given some health information about the person’s lifestyle? In this
study, we will use different machine learning techniques to build a
model which role would be to predict if a person is suffereing from
diabetes or not. The model will use the person’s health information to
classify the person as either a person who has diabete or does not have
diabete.

# Methods

## Data

The data set used in this project to predict diabetes is taken from the
Center for Disease Control and Prevention (CDC), through the Behavioral
Risk Factor Surbellance System (BRFSS) for the year of 2015. This
dataset is collected annually by the CDC, via a phone survey of over
400,000 Americans on health-related risk behaviours, chronic health
conditions, and the use of preventative services. Details of this
dataset can be found
[here](https://www.cdc.gov/brfss/annual_data/annual_2015.html).

## Analysis

# Results and Discussion

<img src="../results/distribution.png" alt="Figure 1. Distribution of every feature" width="60%" />

# References

\[“Zelle (2004)”\]

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-zelle2004python" class="csl-entry">

Zelle, John M. 2004. *Python Programming: An Introduction to Computer
Science*. Franklin, Beedle & Associates, Inc.

</div>

</div>
