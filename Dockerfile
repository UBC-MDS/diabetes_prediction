# Dockerfile for diabetes-prediction project

FROM jupyter/scipy-notebook

USER root

RUN apt-get update

RUN conda install -c conda-forge --quiet --yes \ 
    'matplotlib>=3.2.2' \ 
    'requests>=2.24.0' \
    'graphviz' \
    'python-graphviz' \
    'eli5' \
    'shap' \
    'jinja2' \
    'altair_saver' \
    'selenium<4.3.0' \
    'imbalanced-learn' \
    'pip' \
    'lightgbm' \
    'openpyxl'


RUN apt-get install -y chromium-chromedriver

RUN pip install docopt-ng

# Install R packages
RUN conda install -c conda-forge --quiet --yes \
    'r-base=4.2.1' \
    'r-rmarkdown' \
    'r-tidyverse=1.3*' \
    'r-kableExtra'

# install R packages
RUN Rscript -e "install.packages('knitr', repos = 'http://cran.us.r-project.org')"
