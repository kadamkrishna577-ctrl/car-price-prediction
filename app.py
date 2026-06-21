import streamlit as st
import pickle
import pandas as pd

pipe = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('Cleaned_Car.csv')

st.title("🚗 Car Price Predictor")

company = st.selectbox("Company", sorted(car['company'].unique()))
car_name = st.selectbox("Car Name", sorted(car['name'].unique()))
year = st.selectbox("Year", sorted(car['year'].unique(), reverse=True))
fuel = st.selectbox("Fuel Type", car['fuel_type'].unique())
kms = st.number_input("Kilometers Driven", min_value=0)

if st.button("Predict Price"):
    input_df = pd.DataFrame(
        [[car_name, company, year, kms, fuel]],
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
    )

    price = pipe.predict(input_df)[0]

    st.success(f"Estimated Price: ₹ {price:,.0f}")