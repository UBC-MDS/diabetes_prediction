# Diabetes Prediction

Contributors:
- Flora Ouedraogo
- Austin Shih
- Roan Raina
- Mehdi Naji

## Introduction
Diabetes is a group of diseases that affects an estimated 34.2 million people in the United States [1]. Diabetes occrs when the body is unable to produce or properly use insulin. Insulin, which is produced by the pancreas, regulates the amount of glucose in the blood, often refered to as blood sugar. An individuals blood sugar must stay within a specific range, both high and low blood sugar can cause sever health complications including organ damage. 

Diabetes research has identified various risk factors associated with an increased risk for having diabetes. Risk factors include: weight, age, physical activity, and family history [2]. 

Using the Center for Disease Control and Prevention (CDC) Behavioral Risk Factor Surveillance System (BRFSS) for the year of 2015 [3], our teams seeks to adress the following research question.

## Research Question 

Given an individual's risk factors can we predict if they have diabetes?


## Usage

To replicate the analysis, clone this GitHub repository, install the [dependencies](#dependencies) listed below, and:

run the following command in the terminal from the root directory of this project:

```
make all
```

To clean the data and results generated: 

run the following command in terminal from the root directory of this project:

```
make clean
```

## Report

The final report can be found [here](https://github.com/UBC-MDS/diabetes_prediction/blob/main/doc/diabetes_report.html)

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
- `requests`
- `openpyxl`

## License 

This project ( diabete prediction) is  licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0). If re-using/re-mixing please provide attribution and link to this webpage.
## References

1.  “Diabetes statistics,” National Institute of Diabetes and Digestive and Kidney Diseases. [Online]. Available: https://www.niddk.nih.gov/health-information/health-statistics/diabetes-statistics. [Accessed: 26-Nov-2022]. 

2. “Diabetes risk factors,” Centers for Disease Control and Prevention, 05-Apr-2022. [Online]. Available: https://www.cdc.gov/diabetes/basics/risk-factors.html. [Accessed: 26-Nov-2022]. 

3. The CDC BRFSS survey can be accessed [here](https://www.cdc.gov/brfss/annual_data/annual_2015.html).
