import streamlit as st
import joblib
import pandas as pd

# సేవ్ చేసిన మోడల్ మరియు డేటాను లోడ్ చేయడం
model = joblib.load('olympic_model.pkl')

st.title("🥇 Olympic Medal Prediction App")
st.write("Enter the details to predict the expected number of medals!")

# యూజర్ నుండి ఇన్‌పుట్ తీసుకోవడం
total_athletes = st.number_input("Total Athletes", min_value=1, max_value=1000, value=50)
prev_medals = st.number_input("Previous Medals", min_value=0, max_value=500, value=10)

if st.button("Predict Medals"):
    # ప్రిడిక్షన్ చేయడం
    input_data = pd.DataFrame([[total_athletes, prev_medals]], columns=['total_athletes', 'prev_medals'])
    prediction = model.predict(input_data)
    
    # నెగటివ్ వాల్యూస్ రాకుండా సున్నాకి రౌండ్ చేయడం
    final_pred = max(0, round(prediction[0]))
    
    st.success(f"Estimated Medals: {final_pred}")
