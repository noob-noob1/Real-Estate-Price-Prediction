import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import streamlit as st

# Set the page title and description
st.title("Real_Estate Price Prediction")
st.write("""
This app predicts the price of different houses.
""")

# # Optional password protection (remove if not needed)
# password_guess = st.text_input("Please enter your password?")
# # this password is stores in streamlit secrets
# if password_guess != st.secrets["password"]:
#     st.stop()

# Load the pre-trained model
rf_pickle = open("models/RFmodel.pkl", "rb")
rf_model = pickle.load(rf_pickle)
rf_pickle.close()


# Prepare the form to collect user inputs
with st.form("user_inputs"):
    st.subheader("Housing Details")
    
    # Year sold
    Housing_Year_Sold = st.number_input("Enter when the Year House was Sold", 
                                    min_value=1990, 
                                    max_value=2025, 
                                    step=1)
    
    # Tax
    Property_Tax = st.number_input("Enter Property Tax Amount", 
                               min_value=0, 
                               max_value=10000, 
                               step=100)
    
    # Insurance 
    Insurance = st.number_input("Enter Insurance Amount", 
                            min_value=0, 
                            max_value=3000, 
                            step=10)
    
    # Number of beds
    Number_of_Beds = st.number_input("Enter Number of Bedrooms", 
                                 min_value=0, 
                                 max_value=5, 
                                 step=1)
    # Number of baths
    Number_of_Baths = st.number_input("Enter Number of Bathrooms", 
                                  min_value=1, 
                                  max_value=6, 
                                  step=1)
    
    # Square Feet
    Square_Feet = st.number_input("Enter Property Size (Square Feet)", 
                              min_value=500, 
                              max_value=10000, 
                              step=50)
    
    # Year Built
    Year_Built = st.number_input("Enter the Year Property was Built", 
                             min_value=1880, 
                             max_value=2025, 
                             step=1)

    
    # Lot Size
    Lot_Size = st.number_input("Enter Lot Size (Square Feet)", 
                           min_value=0, 
                           max_value=500000, 
                           step=500)
    
    # Basement
    Basement = st.selectbox("Does the Property Have a Basement?", [0, 1], 
                        format_func=lambda x: "Yes" if x == 1 else "No")

    # Bathrooms
    Popular = st.selectbox("Is the Property Popular?", [0, 1], 
                        format_func=lambda x: "Yes (2 Beds, 2 Baths)" if x == 1 else "No")

    #Recession
    Recession = st.number_input("Was it during the recession? (2010-2013, 1 = Yes, 0 = No)", 
                            min_value=0, 
                            max_value=1, 
                            step=1)
    
   # Calculate Property Age
    Property_Age = Housing_Year_Sold - Year_Built

    # Display Property Age as a read-only input
    st.number_input(
        "Property Age (Years)",
        value=Property_Age,
        disabled=True
    )
    # Bungalow or not
    Bungalow = st.selectbox("Is the Property a Bungalow?", [0, 1], 
                         format_func=lambda x: "Yes" if x == 1 else "No")

    # Condow or not
    Condo = st.selectbox("Is the Property a Condo?", [0, 1], 
                     format_func=lambda x: "Yes" if x == 1 else "No")

    
   
    
    # Submit button
    submitted = st.form_submit_button("Predict Loan Eligibility")


# Handle the dummy variables to pass to the model
if submitted:

    # Making sure we are getting values in integer format
    year_sold= int(Housing_Year_Sold)
    property_tax= int(Property_Tax)
    insurance= int(Insurance)
    beds= int(Number_of_Beds)
    baths= int(Number_of_Baths)
    sqft= int(Square_Feet)
    year_built= int(Year_Built)
    Lot_size= int(Lot_Size)
    basement= int(Basement)
    popular= int(Popular)
    recession= int(Recession)
    property_age= int(Property_Age)
    property_type_Bunglow= int(Bungalow)
    property_type_Condo= int(Condo)
    
    
  

    # Prepare the input for prediction. This has to go in the same order as it was trained
    prediction_input = [[year_sold, property_tax, insurance, beds, baths, sqft,
       year_built, Lot_size, basement, popular, recession,
       property_age, property_type_Bunglow, property_type_Condo
    ]]

    # Make prediction
    new_prediction = rf_model.predict(prediction_input)

    # Display result
    st.subheader("Predicted House Price:")
    st.write(f" ${new_prediction[0]:,.2f}")

st.write(
    """We used a machine learning (Random Forest) model to predict your eligibility, the features used in this prediction are ranked by relative
    importance below."""
)

