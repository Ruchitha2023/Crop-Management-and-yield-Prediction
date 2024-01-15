import streamlit as st
import pandas as pd
import os
st.title("Add a new crop")
with st.form("user_input_form"):
    st.write("Enter your answers:")
    crop = st.text_input("New Crop")
    N = st.text_input("Nitrogen")
    P = st.text_input("Phosphorus")
    K = st.text_input("Potassium")
    temp = st.text_input("Temperature")
    hum = st.text_input("humidity")
    ph = st.text_input("Ph value")
    rainfall = st.text_input("Annual_Rainfall")
    submit_button = st.form_submit_button("Submit")
csv_file_path = "SmartCrop-Dataset.csv"
data = pd.DataFrame(columns=["N", "P", "K","temperature","humidity","ph","rainfall", "label"])
if os.path.exists(csv_file_path):
    data = pd.read_csv(csv_file_path)
if submit_button:
    
    t=float(temp)
    h=float(hum)
    p_h=float(ph)
    r=float(rainfall)
    
    if t>52:
        st.write("*temperature should be less than 44 degree celcius")
    elif h>150:
        st.write("*humidity should be less than 100")
    elif p_h>=10:
        st.write("*ph should be less than 10")
    elif r>298:
        st.write("*rain fall should be less than 298")
    else:
        new_row = {"N": N, "P": P, "K": K, "temperature": temp, "humidity": hum, "ph": ph, "rainfall": rainfall, "label": crop}
        data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
        data.to_csv(csv_file_path, index=False)
        st.success("Crop updated successfully!")
st.write("Current data:")
st.write(data)
st.download_button(
        label="Download CSV File",
        data=data.to_csv(index=False).encode("utf-8"),
        file_name="Updated.csv",
        mime="text/csv",
    )
