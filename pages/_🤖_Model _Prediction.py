import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

sclr = StandardScaler()

st.sidebar.caption("**Collaborators:**\n Clara, Mateus e Silas")

# loading models
# df = pickle.load(open('df.pkl', 'rb'))
# rfc = pickle.load(open('rfc.pkl', 'rb'))

def prediction(credit_score, country, gender, age, tenure, balance, products_number, credit_card, active_member, estimated_salary):
    # Check for empty strings and handle accordingly
    if credit_score == '':
        st.error("Please provide a valid credit score.")
        return None
    if country == '':
        st.error("Please provide a valid country.")
        return None
    if gender == '':
        st.error("Please provide a valid gender.")
        return None
    if age == '':
        st.error("Please provide a valid age.")
        return None
    if tenure == '':
        st.error("Please provide a valid tenure.")
        return None
    if balance == '':
        st.error("Please provide a valid balance.")
        return None
    if products_number == '':
        st.error("Please provide a valid number of products.")
        return None
    if credit_card == '':
        st.error("Please provide a valid credit card status.")
        return None
    if active_member == '':
        st.error("Please provide a valid active member status.")
        return None
    if estimated_salary == '':
        st.error("Please provide a valid estimated salary.")
        return None

    # features = np.array([[float(credit_score), country, gender, float(age), float(tenure), float(balance), float(products_number), float(credit_card), float(active_member), float(estimated_salary)]])
    # features = sclr.fit_transform(features)  # Scale the country column
    # prediction = rfc.predict(features).reshape(1, -1)
    return prediction[0]

# web app
st.title('Bank Customer Churn Prediction')
credit_score = st.number_input('Credit Score')
country = st.text_input('Country')
gender = st.text_input('Gender')
age = st.number_input('Age')
tenure = st.number_input('Tenure')
balance = st.number_input('Balance')
products_number = st.number_input('Products Number')
credit_card = st.number_input('Credit Card')
active_member = st.number_input('Active Member')
estimated_salary = st.number_input('Estimated Salary')

if st.button('Predict'):
    pred = prediction(credit_score, country, gender, age, tenure, balance, products_number, credit_card, active_member, estimated_salary)

    if pred is not None:
        if pred == 1:
            st.write("The customer has left.")
        else:
            st.write("The customer is still active.")
