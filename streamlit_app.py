import streamlit as st
import os
import pickle
st.title("Diabetes Prediction with ML")
working_dir=os.path.dirname(os.path.abspath(__file__))
diabetes_model=pickle.load(open(f'{working_dir}/diabetes_model.sav','rb'))
gender=st.text_input("Enter Gender")
age=st.text_input("Enter Age ")
hp=st.text_input("Enter hypertension")
hd=st.text_input("Enter Heart_disease")
sh=st.text_input("Enter Smoking_history")
bmi=st.text_input("Enter BMI")
hml=st.text_input("Enter Hemoglobin Level")
bgl=st.text_input("Enter Blood Glucode Level")
if st.button("Check Results"):
  user_input=[gender,age,hp,hd,sh,bmi,hml,bgl]
  user_input=[float(x) for x in user_input]
  dia_pred=diabetes_model.predict([user_input])
  if dia_pred[0]==1:
    result="You are diabetic"
  else:
    result="You are not diabetes"
  st.success(result)
