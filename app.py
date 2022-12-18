import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
import sklearn

def app():
    
    model = joblib.load('model.h5')
    st.set_page_config(page_title="Machine Learning Deployment",page_icon=':airplane:',layout="wide")
    st.header("Machine Learning Deployment")
    st.write('start')
    
    
    
    
  
    airline = st.selectbox('Airline', ['Air India', 'Vistara', 'SpiceJet','AirAsia','GO FIRST','Indigo','Trujet','StarAir'])
    departure_time = st.selectbox('departure time', ['Evening', 'Afternoon','Early morning','morning','Night'])
    arriving_time = st.selectbox('arriving time', ['Evening', 'Afternoon','Early morning','morning','Night'])
    fr = st.selectbox("from", ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata','Chennai','Hyderabad'])
    to = st.selectbox("to", ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata','Chennai','Hyderabad'])
    cl = st.radio("Class",['Business','Economy'])
    if_stop = st.radio("Stops",[0,1,2])
    d_date = st.date_input("Departure date")
    
    predict=st.button('Predict')
    
    if predict:
    
    
        df=pd.DataFrame(
            {
                'airline':[0 if airline == 'Air India' else (1 if airline == 'AirAsia' else (2 if airline == 'GO FIRST' else (3 if airline == 'Indigo' else (4 if airline == 'SpiceJet' else (5 if airline == 'StarAir' else (6 if airline == 'Trujet' else  7 )))) ))],
                'departure time':[0 if departure_time == 'Afternoon' else (1 if departure_time == 'Early morning' else (2 if departure_time == 'Evening' else (3 if departure_time == 'Morning' else  4 )))],
                'arriving time':[0 if arriving_time == 'Afternoon' else (1 if arriving_time == 'Early morning' else (2 if departure_time == 'Evening' else (3 if departure_time == 'Morning' else  4 )))],
                'from':[0 if fr == 'Bangalore' else (1 if fr == 'Chennai' else (2 if fr == 'Delhi' else (3 if fr == 'Hyderabad' else (4 if fr =='Kolkata' else 5))))],
                'to':[0 if to == 'Bangalore' else (1 if to == 'Chennai' else (2 if to == 'Delhi' else (3 if to == 'Hyderabad' else (4 if to =='Kolkata' else 5))))],
                'class':[1 if cl=='Business' else 0],
                'if_stop':[if_stop],
                'days left':[(datetime.strptime(str(d_date), '%Y-%m-%d') - datetime.now()).days]
                
            }
        )
        st.dataframe(df)
        
        pred = model.predict(df)
        st.write(F"Price in rubee: {pred}")
   
app()