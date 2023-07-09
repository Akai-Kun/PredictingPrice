import streamlit as st
# import pickle5 as pickle
def main():
    style = """<div style='background-color:pink; padding:12px'>
              <h1 style='color:black'>House Price Prediction App</h1>
       </div>"""
    st.markdown(style, unsafe_allow_html=True)
    left, right = st.columns((2,2))
    longitude = left.number_input('Enter the Longitude in negative number',step =1.0, format="%.2f", value=-21.34)
    latitude = right.number_input('Enter the Latitude in positive number',step=1.0, format='%.2f', value= 35.84)
    housing_median_age = left.number_input('Enter the median age of the building',step=1.0, format='%.1f', value=25.0)
    total_rooms = right.number_input('How many rooms are there in the house?',step=1.0, format='%.1f', value=56.0)
    total_bedrooms = left.number_input('How many bedrooms are there in the house?',step=1.0, format='%.1f', value=15.0)
    population = right.number_input('Population of people within a block',step=1.0, format='%.1f', value=250.0)
    households = left.number_input('Poplulation of a household',  step=1.0,format='%.1f',value=43.0)
    median_income = right.number_input('Median_income of a household in Dollars',step=1.0, format='%.1f', value=3000.0)    
    ocean_proximity = st.selectbox('How close to the sea is the house?',('<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR BAY', 'ISLAND'))
    button = st.button('Predict')
    
    # if button is pressed
    if button:
        
        # make prediction
        result = predict(longitude, latitude, housing_median_age,
                         total_rooms,total_bedrooms, population,
                         households, median_income, ocean_proximity)
        st.success(f'The value of the house is ${result}')