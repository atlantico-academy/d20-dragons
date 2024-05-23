import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle
import joblib
sclr = StandardScaler()

st.sidebar.caption("**Collaborators:**\n Clara, Mateus e Silas")

#   loading models
xgb = joblib.load('.\models\pipeline_model.pkl')

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
    
    features = [[float(credit_score), country, gender, float(age), float(tenure), float(balance), float(products_number), float(credit_card), float(active_member), float(estimated_salary)]]
    colunas = ['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']
    features = pd.DataFrame(features,columns=colunas)
    print(features)
    prediction = xgb.predict(features)
    
    
    return prediction[0]

# web app
st.title('Bank Customer Churn Prediction')
credit_score = st.number_input('Credit Score')
country = st.selectbox('Country',['Germany','Spain','France'])
gender = st.selectbox('Gender',['Male','Female'])    
age = st.number_input('Age',step=1)
tenure = st.number_input('Tenure',step=1,min_value=0,max_value=10)
balance = st.number_input('Balance')
products_number = st.number_input('Products Number',min_value=0,max_value=4,step=1)
credit_card = st.selectbox('Credit Card',['Yes','No'])
active_member = st.selectbox('Active Member',['Yes','No'])
estimated_salary = st.number_input('Estimated Salary')

credit_card = 1 if credit_card == 'Sim' else 0
active_member = 1 if active_member == 'Sim' else 0

# Mapeamento de variáveis categóricas
#country_mapping = {'Germany': 0, 'Spain': 1, 'France': 2}
#gender_mapping = {'Male': 0, 'Female': 1}

#country = country_mapping[country]
#gender = gender_mapping[gender]
    
    
if st.button('Predict'):
    pred = prediction(credit_score, country, gender, age, tenure, balance, products_number, credit_card, active_member, estimated_salary)

    if pred is not None:
        if pred == 1:
            st.write("The customer has left.")
        else:
            st.write("The customer is still active.")
