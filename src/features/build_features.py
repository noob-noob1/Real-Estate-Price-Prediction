import pandas as pd

# create dummy features
def Split_Data(df):
    
    # seperate input features in x
    X = df.drop('price', axis=1)

    # store the target variable in y
    y = df['price']

    return X, y