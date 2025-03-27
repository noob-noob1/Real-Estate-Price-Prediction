# Real Estate Price Prediction
[Visit the app here](https://real-estate-price-prediction-mc8qmxxkwgmsq85lrzrscs.streamlit.app/)

This application predicts the price of a house based on its input features. It aims to help end users assess the price of a property without the need for a real estate agent. The app is built using Streamlit, a popular open-source framework for creating web applications with Python.

## Features 
1. User-friendly interface for inputting property details
2. Real-time price prediction based on input features
3. Easy-to-use and accessible for a wide range of users

## Dataset

The app is trained on the real-estate dataset, the original dataset csv could be found in the data section of this repository. The features of the dataset are as follows:
- Price
- Year Sold
- Property Tax
- Insurance
- Beds
- Baths
- Square Footage (Sqft)
- Year Built
- Lot Size
- Basement

And after feature engineering, the following features have been added:
- Popular : If it is 2 beds and 2 baths
- Recession: If year sold between 2010 and 2013
- Property Age: Year built - year sold
- Property Type: Bungalow
- Property Type: Condo

## Technologies used
- Streamlit :App debvelopemnt and deployement
- Python: General coding 
- Pandas and NumPy: Data manipulation and processing
- Scikit-learn: Model training and evaluation
- Matplotlib and Seabor: EDA and visualization

## Model

The model that was picked for deployement was RandomForest, it performed by far the best with **MAE** == 43736.91 which is under the 7000 threshhold we had as a bechmark for our results

## Installation (for local deployment)
If you want to run the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/noob-noob1/Real-Estate-Price-Prediction.git
   cd Real Estate Dataset Project

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\\Scripts\\activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Streamlit application:
   ```bash
   streamlit run streanlit.py




# Project Organization

Modularizing and developing a streamlit app for the famous real estate dataset
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
