import streamlit as st
import pickle 
import numpy as np
from sklearn.linear_model import LogisticRegression


st.title("Check the environment")

#input  dtaa
carbon_emission =st.number_input("Carbon emission amount", min_value=0.0, format="%f")

energy_output =st.number_input("Energy output value", min_value=0.0, format="%f")

renewablitiy_index =st.number_input("Renewablitiy index  amount", min_value=0.0, format="%f")

Cost_efficency =st.number_input("Cost Efficency amount", min_value=0.0, format="%f")



#model importing
with open('logistic_regression_model2.pkl', 'rb')as file :
    model =pickle.load(file)

#predict
if st.button("predict"):
    input_data =np.array([[carbon_emission, energy_output, renewablitiy_index, Cost_efficency]])

    prediction =model.predict(input_data)

    #diaplay result
    if prediction[0]==1:
        st.success("congrats the environment is sustainabale")
    else:
        st.info("It is not sustainable")
