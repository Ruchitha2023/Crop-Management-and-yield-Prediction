import streamlit as st
import pandas as pd
import numpy as np
import os
import base64
import pickle

model = pickle.load(open('model1.pkl','rb'))
sc = pickle.load(open('standscaler1.pkl','rb'))
ms = pickle.load(open('minmaxscaler1.pkl','rb'))

st.title("Crop  prediction")
with st.form("user_input_form"):
    st.write("Enter your answers:")
    N = st.text_input("Nitrogen")
    P = st.text_input("Phosphorus")
    K = st.text_input("Potassium")
    temp = st.text_input("Temperature('C)")
    hum = st.text_input("humidity")
    ph = st.text_input("Ph value")
    rainfall = st.text_input("Annual_Rainfall(cm)")
    
    
    submit_button = st.form_submit_button("Predict")
    
    
if submit_button:
    n=int(N)
    p=int(P)
    k=int(K)
    t=float(temp)
    h=float(hum)
    p_h=float(ph)
    r=float(rainfall)
    
    feature_list = [N, P, K, temp, hum, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)
    #n=single_pred[0]
    if n>140 or n<0:
        st.write("*value should be less than 140 and more than 1")
    elif p>145 or n<5:
        st.write("*value should be less than 145 and more than 4")
    elif k>205 or k<5:
        st.write("*value should be less than 205 and more than 4")
    elif t>42 or t<8.825:
        st.write("*temperature should be less than 42 and more than 8.8 degree celcius")
    elif h>100 or h<14.25:
        st.write("*humidity should be less than 100 and more than 14.25")
    elif p_h>=10 or p_h<3.5:
        st.write("*ph should be less than 10 and more than 3.5")
    elif r>298 or r<20.2:
        st.write("*rain fall should be less than 298 and more than 20.2")
    else:
        scaled_features = ms.transform(single_pred)
        final_features = sc.transform(scaled_features)
        prediction = model.predict(final_features)
    
        crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

        if prediction[0] in crop_dict:
            crop = crop_dict[prediction[0]]
            result = "{} is the best crop to be cultivated right there".format(crop)
            st.write(f"# {result}")
            #st.write(result)
        else:
            result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
            st.write(result)