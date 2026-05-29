import streamlit as st
import joblib
import numpy as np

st.title("Salary Predictions Application")

st.divider()

st.write("This application predicts the salary of company employees.")

years=st.number_input("Enter years of experience:", value=1, step=1, min_value=0)
jobrate=st.number_input("Enter job rate:", value=3.5, step=0.5, min_value=0.0)

x=[years,jobrate]

model=joblib.load("model.joblib")

predict=st.button("Predict Salary")

st.divider()

if predict:
    st.write("Predicting salary...")
    st.balloons()
    x1=np.array([x])
    predict=model.predict(x1)[0]
    st.write(f"Salary Prediction is: {predict:.2f}")

else:
    st.write("Please press the button to predict the salary.")