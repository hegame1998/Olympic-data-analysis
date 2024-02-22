import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
        page_title="📏 Correlation",
        layout="wide",
    )

st.subheader("📏 Correlation")
st.text('Please choose the dataset that you want to see below.')


# datasets
athlete_df = pd.read_csv('https://raw.githubusercontent.com/MaH1996SdN/programming_project/master/athlete_events.csv')
regions_df = pd.read_csv('https://raw.githubusercontent.com/MaH1996SdN/programming_project/master/noc_regions.csv')

# drop & merge
regions_df.drop('notes', axis=1, inplace=True)
athlete_df=pd.merge(athlete_df, regions_df, on='NOC', how='left')
athlete_df.rename(columns = {'region':'Country'}, inplace = True)
athlete_df.drop(['ID','Team', 'NOC', 'Games', 'City'], axis=1, inplace=True)

# cleaning 
athlete_df['Medal'].fillna('non-Medal', inplace = True)
athlete_df.Medal.replace({'Gold':1, 'Silver':2, 'Bronze':3, 'non-Medal':0}, inplace=True)
athlete_df['Country'].fillna('Unknown-Country', inplace = True)

# filling null values 
athlete_df['Age'].fillna(athlete_df['Age'].mean(), inplace = True)
athlete_df['Height'].fillna(athlete_df['Height'].mean(), inplace=True)
athlete_df['Weight'].fillna(athlete_df['Weight'].mean(), inplace=True)


# Select specific columns for correlation analysis
selected_columns = ['Medal', 'Year', 'Weight', 'Height', 'Age']  
correlation_matrix = athlete_df[selected_columns].corr()
fig, ax = plt.subplots(figsize=(10,6))




# Store the initial value of widgets in session state
if "display_option" not in st.session_state:
    st.session_state.display_option = "Correlation"

col1, col2 = st.columns([1, 2])

with col1:
    st.radio(
        "Select one item:",
        key="display_option",
        options=["Correlation", "Heatmap"],
    )

with col2:
    if st.session_state.display_option == "Correlation":
        st.write("Correlation of data:")
        st.write(correlation_matrix)
    elif st.session_state.display_option == "Heatmap":
        st.write("Heatmap of data:")
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
        st.pyplot(fig)


