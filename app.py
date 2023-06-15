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

# Get the citites
city = st.select(
    "Select the city where the match is being played", sorted(cities)
)

# input target
target = st.number_input("Target")

col_3, col_4, col_5 = st.columns(3)

with col_3:
    score = st.number_input("Current Score")

with col_4:
    overs = st.number_input("Overs Completed")

with col_5:
    wickets = st.input_number("Wicket Fallen")

if st.button("Predict Probability"):

    runs_left = target - score 
    balls_left = 120 - (overs * 6)
    wickets = 10 - wickets 
    current_run_rate = score / overs
    required_run_rate = (runs_left * 6) / balls_left

# get the input data into a dataframe
input_df = pd.DataFrame({
    'batting_team': [batting_team], 
    'bowling_team': [bowling_team], 
    'city': [city], 
    'runs_left': [runs_leftt], 
    'balls_left': [balls_left],
    'wickets': [wickets], 
    'total_runs_x': [target], 
    'cur_run_rate': [current_run_rate], 
    'req_run_rate': [required_run_rate]
})