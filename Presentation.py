import pandas as pd
import numpy as np
import streamlit as st


st.header("Presentation of Final Project")
st.subheader("Programming & Database")

<br>

athlete_df = pd.read_csv('https://raw.githubusercontent.com/MaH1996SdN/programming_project/master/athlete_events.csv')
st.write("The raw data of athlete of olympic:")
st.write(athlete_df)
