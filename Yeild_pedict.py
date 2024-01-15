import streamlit as st
import pandas as pd
import numpy as np
import os
import base64
import pickle


st.title("Crop Yield prediction")
with st.form("user_input_form"):
    st.write("Enter your answers:")
    crop = st.text_input("Crop")
    year = st.text_input("Crop_year")
    season = st.text_input("Season")
    state = st.text_input("State")
    area = st.text_input("Area")
    anual_rainfall = st.text_input("Annual_Rainfall")
    fertilizer = st.text_input("Fertilizer")
    pest = st.text_input("Pesticide")
    
    
    submit_button = st.form_submit_button("Predict")
#csv_file_path = "headbrain.csv"
#data = pd.DataFrame(columns=["Crop", "Crop_year", "Season"])
#if os.path.exists(csv_file_path):
   # data = pd.read_csv(csv_file_path)
    dtr = pickle.load(open('dtr.pkl','rb'))
    preprocessor = pickle.load(open('preprocessor.pkl','rb'))
    
if submit_button:
    #new_row = {"Crop": name, "Crop_year": age, "Season": email}
    #data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
    #data.to_csv(csv_file_path, index=False)
    a=float(anual_rainfall)
    f=float(fertilizer)
    p=float(pest)
    if a>300:
        st.write("It should be less than 200")
            
    else:
        features = np.array([[crop,year,season,state,area,anual_rainfall,fertilizer,pest]],dtype=object)
        transformed_features = preprocessor.transform(features)
        prediction = dtr.predict(transformed_features).reshape(1,-1)
        pred = prediction*10
        #pred =print(pred)
        st.write(f"# {pred}")
        st.write("Quintal per hector")
        st.success("Yeild Predcted successfully!")
    

