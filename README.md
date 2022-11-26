# Predicting if a person has diabete or not

Contributors:  
- Flora Ouedraogo
- Austin Shih
- Roan Raina
- Mehdi Naji

### Goal: This project aims to build a model which will be able to predict if a patient has diabete or not given some information about his/her health indicators.


## Introduction
Diabete is a disease which affects many people around the world. This disease is the result of the lack of insulin in the body. Insulin is a hormone produced by your pancreas whose role is to regulate the amount of glucose in the blood. Blood sugar must be carefully regulated to ensure that the body functions properly. Too much blood sugar can damage some organs, like blood vessels and nerves. Our body also needs insulin in order to use sugar for energy. According to the International Diabetes Federation “In 2021, Approximately 537 million adults (20-79 years) are living with diabetes. The total number of people living with diabetes is projected to rise to 643 million by 2030 and 783 million by 2045”.
With these alarming figures, many experts claim that it is important to have a good  lifestyle, i.g. physical activity and good eating habits, in order to avoid this disease or avoid its complicated form. Can we really tell if a person is suffering from diabetes or not, given some health information about the person's lifestyle?


## Research Question 

Given a person's health indicators (BMI, smoker, physical activity), is he or she having diabete?


## Usage

To replicate the analysis, clone this GitHub repository, install the [dependencies](#dependencies) listed below, and:


Run the following command to download the data:
```
python src/download_data.py --url=https://www.cdc.gov/brfss/annual_data/2015/files/LLCP2015XPT.zip --out_dir=data/raw
```

Run the following command to clean the downloaded data:

```
python src/clean.py --in_file="data/raw/LLCP2015.XPT " --out_file="data/clean/LLCP2015_clean.csv"
```


Run the following command for predictions 

```
 python predictions.py --clean_data=../data/clean/LLCP2015_cleaned.csv --output_file='../results'
```

Run the following command to produce the report

```
Rscript -e "rmarkdown::render('doc/breast_cancer_predict_report.Rmd', output_format = 'github_document')"
```
## The Data Set

The data set used in this project to predict diabetes is taken from the Center for Disease Control and Prevention (CDC), through the Behavioral Risk Factor Surbellance System (BRFSS) for the year of 2015. This dataset is collected annually by the CDC, via a phone survey of over 400,000 Americans on health-related risk behaviours, chronic health conditions, and the use of preventative services. Details of this dataset can be found [here](https://www.cdc.gov/brfss/annual_data/annual_2015.html).

We modified and cleaned the fulL CDC dataset to include only project relevant variables following a approach used by Alex Teboul in `Diabetes Health Indicators Dataset Notebook` on Kaggle found [here](https://www.kaggle.com/code/alexteboul/diabetes-health-indicators-dataset-notebook/notebook).

The dataset consist of 22 columns; one target and 21 feature variables. We found from our EDA that there does exist class imbalance in the dataset. Each row in our dataset represents health indicators from every respondent. The target variable, `Diabetes_012`,  has three classes:
* 0 : no diabetes or only during pregnancy,
* 1 : for prediabetes, 
* 2 : diabetes. 

### The feature variables in this dataset includes: 

|Variabl | Type | Question | Values |
| -------|------|-----| -------|
|**HighBP** | binary | high BP? | 0 = no & 1 = yes |
|**HighChol** |binary | high cholesterol? | 0 = no & 1 = yes |
| **CholCheck**| binary| cholesterol check in 5 years?| 0 = no & 1 = yes |
|**BMI**| numeric| Body Mass Index | |
|**Smoker**| binary| smoked at least 100 cigarettes in your entire life?| 0 = no & 1 = yes |
|**Stroke** | binary| ever told you had a stroke?| 0 = no & 1 = yes|
|**HeartDiseaseofAttack**| binary| coronary heart disease(CHD) or myocardial infarction(MI)?| 0 = no & 1 = yes|
|**PhysActivity**| binary| physical activity in past 30 days - not including job?| 0 = no & 1 = yes|
|**Fruits**| binary| consume fruit 1 or more times per day?| 0 = no & 1 = yes|
|**Veggies**| binary| consume vegetables 1 or more times per day?| 0 = no & 1 = yes|
|**HvyAlcoholConsump**| binary| Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week)| 0 = no & 1 = yes|
|**AnyHealthcare**| binary| any kind of heath care coverage?| 0 = no & 1 = yes|
|**NoDocbcCost**| binary| Was there a time in past 12 months, you needed to see a doctor but could not due to the cost?| 0 = no & 1 = yes|
|**GenHlth**|ordinal | Would you say that in general your health is: | 1 = excellent <br> 2 = very good <br> 3 = good <br> 4 = fair <br> 5 = poor|
|**MentHlth**| ordinal| how many days of poor mental health during last 30 days?| from 1 to 30|
|**PhysHlth**| ordinal| how many days of poor physical health during last 30 days?| from 1 to 30|
|**DiffWalk**| binary| do you have serious difficulty walking or climbing stairs?| 0 = no & 1 = yes|
|**Sex**| binary|Indicate sex of respondent.| 0 = female & 1 = male|
|**Age**| ordinal|Fourteen-level age category| 13-level age category|
|**Education**| ordinal|What is the highest grade or year of school you completed?| 6-level education category|
|**Income**| ordinal| Is your annual household income from all sources?|8-level income category|

## Project Plan

To answer the above project question, We start by conducting an exploratory data analysis(EDA) on the dataset. Through the EDA, we will be exploring the features more in details to help us make decisions like scaling cilumns or dropping some columns. The problem that we will be tackling in this study is a classification problem. Since it is a classification problem, the possible supervised learning techniques that we might end up exploring will include DecisionTree, Logistic Regression and SVC. After chosing the machine learning technique, we will do hyperparameter tuning to find the best parameter combinations. Since, we are trying to predict wether a person has diabete or not based on health indicators, it is important to analyze feature importance in order to find the feature which is crucial in determining if a person has a diabete or not.
After choosing our final model, we will re-fit the model on the entire training data set after preprocessing and evaluate its performance on the test data set. We will then look at overall accuracy and how our model classified the test data observations. We will use a confusion matrix to present the results of the classification of our model.

## Dependencies
Python:
- `ipykernel`
- `matplotlib>=3.2.2`
- `scikit-learn>=1.1.3`
- `requests>=2.24.0`
- `graphviz`
- `python-graphviz`
- `eli5`
- `shap`
- `jinja2`
- `altair_saver`
- `selenium<4.3.0`
- `pandas<1.5`
- `imbalanced-learn`
- `pip`
- `lightgbm`
- `docopt`
- `pandas`
- `requests`
- `openpyxl`

## License 

This project ( diabete prediction) is  licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0). If re-using/re-mixing please provide attribution and link to this webpage.
## References

- The CDC BRFSS survey can be accessed [here](https://www.cdc.gov/brfss/annual_data/annual_2015.html).
- The referenced Kaggle diabete dataset, Diabetes Health Indicator Dataset, is publicly available for research and can be accessed [here](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)
