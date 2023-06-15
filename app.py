import streamlit as st
import pandas as pd 
import pickle

# Declaring the most common teams 
teams = ['Sunrisers Hyderabad',
         'Mumbai Indians',
         'Royal Challengers Bangalore',
         'Kolkata Knight Riders',
         'Kings XI Punjab',
         'Chennai Super Kings',
         'Rajasthan Royals',
         'Delhi Capitals']

# Delcaring the venues (cities) of the matches
cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']

# load the trained model
pipe = pickle.load(open("pipe.pkl", "rb"))
st.title("IPL Team Win Probability Predictor")

col_1, col_2 = st.columns(2)

with col_1:
    batting_team = st.selectbox("Select the batting team", sorted(teams))

with col_2:
    bowling_team = st.selectbox("Select the bowling team", sorted(teams))