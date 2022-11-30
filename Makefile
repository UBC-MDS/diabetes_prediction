# diabetes prediction data pipe
# author: Austin Shih
# date: 2022-11-29

all: doc/diabetes_report.md

# download data
data/raw/LLCP2015.XPT : src/download_data.py
	python src/download_data.py --url=https://www.cdc.gov/brfss/annual_data/2015/files/LLCP2015XPT.zip --out_dir=data/raw 

# clean data
data/clean/LLCP2015_cleaned.csv : src/clean.py data/raw/LLCP2015.XPT
	python src/clean.py --in_file="data/raw/LLCP2015.XPT " --out_file="data/clean/LLCP2015_cleaned.csv" 

# exploratory data analysis - visualize predictor distributions across classes
results/correlation.xlsx results/distribution.png : src/diabetes_eda.py data/clean/LLCP2015_cleaned.csv
	python src/diabetes_eda.py --clean_data=data/clean/LLCP2015_cleaned.csv --output_file='results' 

# predictions
results/cross_val_results.csv results/final_test_results.csv : src/predictions.py data/clean/LLCP2015_cleaned.csv
	 python src/predictions.py --clean_data=data/clean/LLCP2015_cleaned.csv --output_file='results' 

# render report
doc/diabetes_report.md : doc/diabetes_report.Rmd doc/references.bib results/cross_val_results.csv results/final_test_results.csv results/correlation.xlsx results/distribution.png
	Rscript -e "rmarkdown::render('doc/diabetes_report.Rmd', output_format = 'github_document')" doc/diabetes_report.md

clean: 
	rm -rf data
	rm -rf results