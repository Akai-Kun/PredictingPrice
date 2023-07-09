# Import necessary libraries
import pandas as pd
import streamlit as st
import datetime
import pickle

# Load the CSV file with the car data
pred_df = pd.read_csv("./AB_US_2020.csv")

# Write the title of the application on the UI
st.write("""
# Price Prediction App
""")

# Function to make the prediction using the pre-trained model
def model_pred(reviews, lat, long, id):

    ## Load the pre-trained model using pickle
    with open("USA_database.ipynb", "rb") as file:
        reg_model = pickle.load(file)

    # Prepare the input features
    input_features = [[reviews, lat, long, id]]
    return reg_model.predict(input_features)

# Create two columns in the UI
col1, col2, col3 = st.columns(3)

row1, row2 = st.columns(2)

# Create a textbox to search for the id
id = row1.text_input("ID")

# Create a slider to set the engine power
latitude = row1.slider("Latitude",
                        0, 50, step=1)

# Create a slider to set the engine power
longitude = row1.slider("Longitude",
                        -200, 0, step=1)

# Create a slider to set the engine power
reviews_per_month = row1.slider("Reviews / Month",
                        0, 10, step=1) 





# Create a button to trigger the prediction
if(st.button("Predict Price")):
#   # Encode the categorical variables
#     fuel_type = encode_dict['fuel_type'][fuel_type]
#     transmission_type = encode_dict['transmission_type'][transmission_type]

    # Make the prediction
    price = model_pred(reviews_per_month, latitude, longitude, id)
    
     # Display the result on the UI
    st.text("Predicted price: "+ str(price))

# # Create a bar chart (commented out)
#st.bar_chart(data=cars_df, x= 'fuel_type', y= 'mileage')