# from setuptools import find_packages, setup


# setup(
#     name='src',
#     packages=find_packages(),
#     version='0.1.0',
#     description='Credit Risk Model code structuring',
#     author='Swapnil Kangralkar',
#     license='',
# )

from src.data.make_dataset import load_and_preprocess_data
from src.models.train_model import train_RFmodel
from src.models.predict_model import evaluate_model
from src.features.build_features import Split_Data


if __name__ == "__main__":
    # Load and preprocess the data
    data_path = r"data\raw\final.csv"
    df = load_and_preprocess_data(data_path)
    X, y = Split_Data(df)

    # Train the random forest regression model
    model, X_test, y_test = train_RFmodel(X, y)

    # Evaluate the model
    MAE = evaluate_model(model, X_test, y_test)
    print(f"MAE: {MAE}")
    
