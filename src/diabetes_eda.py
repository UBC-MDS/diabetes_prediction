# author: Austin Shih
# date: 2022-11-22

"""Takes clean dataset from clean.py and produces exploratory data visualizations to better understand cleaned data.

Usage: diabetes_eda.py --clean_data=<clean_data> --output_file=<output_file>

Options:
--clean_data=<clean_data>       Relative path of cleaned dataset 
--output_file=<output_file>     Relative path to output file directory
"""
# python diabetes_eda.py --clean_data=../data/clean/LLCP2015_cleaned.csv --output_file='../results'

# Imports 
from docopt import docopt
import pandas as pd
import altair as alt
from altair_saver import save
import os

# docopt 
opt = docopt(__doc__)

def main(clean_data, output_file):

    # create result directory
    if os.path.exists(output_file) == False:
        print('Results directory does not exist, creating directory...')
        os.mkdir(output_file)
    else:
        print('Results directory exists')

    # read clean csv
    try:
        df = pd.read_csv(clean_data)        # df = pd.read_csv(../data/clean/LLCP2015_cleaned.csv)
    except FileNotFoundError:
        print("Input csv file of train set does not exist.")
        os._exit()

    # Distributions of complete data set
    df_cols = df.columns.tolist()

    # distribution plots
    df_plot = alt.Chart(df).mark_bar().encode(
        alt.X(alt.repeat(), type='quantitative', bin=alt.Bin(maxbins=60)),
        alt.Y('count()'),
        color = 'Diabetes_012'
    ).properties(
        height=200,
        width=320
    ).repeat(
        df_cols,
        columns = 3)

    # save distribution plot
    try:
        df_plot.save(output_file + '/' +'distribution.png')
        print("distribution plot generation complete")
    except FileNotFoundError as fx:
        print("Error in target file path")
        print(fx)
        print(type(fx))

    # correlation plots
    corr_plot = df.corr('spearman').style.background_gradient() 

    # save correlation plot
    try:
        corr_plot.to_excel(output_file + '/' + 'correlation.xlsx')
        print("correlation csv file generation complete")
    except FileNotFoundError as fx:
        print("Error in target file path")
        print(fx)
        print(type(fx))
    
    # Age distributions of different class of diabetes
    age_dist = (alt.Chart(df)
                   .transform_density(
                        'Age',
                        groupby=['Diabetes'],
                        as_=['Age', 'density'])
                    .mark_area(opacity=0.4).encode(
                        x='Age',
                        y='density:Q',
                        color=alt.Color(
                            'Diabetes', 
                            scale=alt.Scale(scheme='set1'))))
    
    # save age distribution plot
    try:
        age_dist.save(output_file + '/' +'age.png')
        print("age distribution plot generation complete")
    except FileNotFoundError as fx:
        print("Error in target file path")
        print(fx)
        print(type(fx))
        
    # BMI distributions of different class of diabetes
    bmi_dist = (alt.Chart(df)
                   .transform_density(
                        'BMI',
                        groupby=['Diabetes'],
                        as_=['BMI', 'density'])
                    .mark_area(opacity=0.4).encode(
                        x='BMI',
                        y='density:Q',
                        color=alt.Color(
                            'Diabetes', 
                            scale=alt.Scale(scheme='set1'))))
    
    # save bmi distribution plot
    try:
        bmi_dist.save(output_file + '/' +'bmi.png')
        print("bmi distribution plot generation complete")
    except FileNotFoundError as fx:
        print("Error in target file path")
        print(fx)
        print(type(fx)) 
    
    # Income distributions of different class of diabetes
    income_dist = (alt.Chart(df)
                   .transform_density(
                        'Income',
                        groupby=['Diabetes'],
                        as_=['Income', 'density'])
                    .mark_area(opacity=0.4).encode(
                        x='Income',
                        y='density:Q',
                        color=alt.Color(
                            'Diabetes', 
                            scale=alt.Scale(scheme='set1'))))
    
    # save income distribution plot
    try:
        income_dist.save(output_file + '/' +'income.png')
        print("income distribution plot generation complete")
    except FileNotFoundError as fx:
        print("Error in target file path")
        print(fx)
        print(type(fx))   
        
    # Education distributions of different class of diabetes
    education_dist = (alt.Chart(df)
                   .transform_density(
                        'Education',
                        groupby=['Diabetes'],
                        as_=['Education', 'density'])
                    .mark_area(opacity=0.4).encode(
                        x='Education',
                        y='density:Q',
                        color=alt.Color(
                            'Diabetes', 
                            scale=alt.Scale(scheme='set1'))))
    
    # save education distribution plot
    try:
        education_dist.save(output_file + '/' +'education.png')
        print("education distribution plot generation complete")
    except FileNotFoundError as fx:
        print("Error in target file path")
        print(fx)
        print(type(fx))   
    
if __name__ == "__main__":
    main(opt["--clean_data"], opt["--output_file"])
