import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
import sklearn
import geopy
from geopy.geocoders import Nominatim
from geopy import distance

def app():
    
    model = joblib.load('model.h5')
    st.set_page_config(page_title="Machine Learning Deployment",page_icon=':airplane:',layout="wide")
    st.header("Machine Learning Deployment")
    st.write('start')

    departure_time = st.selectbox('departure time', ['Evening', 'Afternoon','Early morning','morning','Night'])
    arriving_time = st.selectbox('arriving time', ['Evening', 'Afternoon','Early morning','morning','Night'])
    cl = st.radio("Class",['Business','Economy'])
    fr = st.text_input("from")
    to = st.text_input("to")
    
    if_stop = st.radio("Stops",[0,1,2,3])
    stops = st.text_input("where are the stops?, if there are more than one stop split between them by a comma (,)")
    
    d_date = st.date_input("Departure date")
    weekend = st.radio("is it a weekend?",['yes','no'])
    
    loc = Nominatim(user_agent="GetLoc",timeout=10)
    if if_stop == 0:
        place1 = loc.geocode(fr)
        place2 = loc.geocode(to)
        
        Loc1_lat, Loc1_lon = (place1.latitude), (place1.longitude)
        Loc2_lat, Loc2_lon = (place2.latitude), (place2.longitude)
        
        location1 = (Loc1_lat, Loc1_lon)
        location2 = (Loc2_lat, Loc2_lon)
        dis=distance.geodesic(location1, location2).km
    elif if_stop == 1:
        place1 = loc.geocode(fr)
        place2 = loc.geocode(to)
        place3 = loc.geocode(stops)
        
        Loc1_lat, Loc1_lon = (place1.latitude), (place1.longitude)
        Loc2_lat, Loc2_lon = (place2.latitude), (place2.longitude)
        Loc3_lat, Loc3_lon = (place3.latitude), (place3.longitude)
        
        location1 = (Loc1_lat, Loc1_lon)
        location2 = (Loc2_lat, Loc2_lon)
        location3 = (Loc3_lat, Loc3_lon)
        dis=distance.geodesic(location1, location2,location3).km
    elif if_stop==2:
        s=stops.split(',')
        place1 = loc.geocode(fr)
        place2 = loc.geocode(to)
        place3 = loc.geocode(s[0])
        place4 = loc.geocode(s[1])
        
        Loc1_lat, Loc1_lon = (place1.latitude), (place1.longitude)
        Loc2_lat, Loc2_lon = (place2.latitude), (place2.longitude)
        Loc3_lat, Loc3_lon = (place3.latitude), (place3.longitude)
        Loc4_lat, Loc4_lon = (place4.latitude), (place4.longitude)
        
        location1 = (Loc1_lat, Loc1_lon)
        location2 = (Loc2_lat, Loc2_lon)
        location3 = (Loc3_lat, Loc3_lon)
        location4 = (Loc4_lat, Loc4_lon)
        dis=distance.geodesic(location1, location2,location3,location4).km
    elif if_stop==3:
        s=stops.split(',')
        place1 = loc.geocode(fr)
        place2 = loc.geocode(to)
        place3 = loc.geocode(s[0])
        place4 = loc.geocode(s[1])
        place5 = loc.geocode(s[2])
        
        Loc1_lat, Loc1_lon = (place1.latitude), (place1.longitude)
        Loc2_lat, Loc2_lon = (place2.latitude), (place2.longitude)
        Loc3_lat, Loc3_lon = (place3.latitude), (place3.longitude)
        Loc4_lat, Loc4_lon = (place4.latitude), (place4.longitude)
        Loc5_lat, Loc5_lon = (place5.latitude), (place5.longitude)
        
        location1 = (Loc1_lat, Loc1_lon)
        location2 = (Loc2_lat, Loc2_lon)
        location3 = (Loc3_lat, Loc3_lon)
        location4 = (Loc4_lat, Loc4_lon)
        location5 = (Loc5_lat, Loc5_lon)
        dis=distance.geodesic(location1, location2,location3,location4,location5).km
        
    
    predict=st.button('Predict')
    
    if predict:
    
    
        df=pd.DataFrame(
            {
                
                'departure time':[0 if departure_time == 'Afternoon' else (1 if departure_time == 'Early morning' else (2 if departure_time == 'Evening' else (3 if departure_time == 'Morning' else  4 )))],
                'arriving time':[0 if arriving_time == 'Afternoon' else (1 if arriving_time == 'Early morning' else (2 if departure_time == 'Evening' else (3 if departure_time == 'Morning' else  4 )))],
                'class':[1 if cl=='Business' else 0],
                'if_stop':[if_stop],
                'days left':[(datetime.strptime(str(d_date), '%Y-%m-%d') - datetime.now()).days],
                'distance':[dis],
                'weekend':[1 if weekend == 'yes' else 0]
                
                
                    
            }   
        )
        st.dataframe(df)
        
        pred = model.predict(df)
        st.write(F"Price in dollar: {pred * 0.014}")
    
app()