import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
        page_title="📈 Line chart",
        layout="wide",
    )

st.subheader("📈 Line chart")
st.text('Please select one item to see the line chart of athletes who won medal.')


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



# Assuming athlete_df is your DataFrame containing athlete data
# Prepare Data
Medals = athlete_df.loc[athlete_df['Medal'] != 0]
Height_weight_data = Medals[['Height', 'Weight']]
# Group by Height and Weight
height_counts = Height_weight_data['Height'].value_counts().sort_index()
weight_counts = Height_weight_data['Weight'].value_counts().sort_index()

# Group by year and sex for count of men and women
woman_counts = Medals.loc[Medals['Sex'] == 'F'].groupby('Year').size()
man_counts = Medals.loc[Medals['Sex'] == 'M'].groupby('Year').size()

# Concatenate dataframes for height and weight counts
HeightWeight_combine = pd.concat([height_counts, weight_counts], axis=1)
HeightWeight_combine.columns = ['Height', 'Weight']
WomanMan_combine = pd.concat([woman_counts, man_counts], axis=1)
WomanMan_combine.columns = ['Man', 'Woman']


# Layout
left_column, right_column = st.columns([1, 3])

with left_column:
    option = st.radio('Select your choose:', ['Height & Weight', 'Men & Women'])
    

with right_column:
    if option == 'Height & Weight':
        st.text('Height vs Weight of Medalists')
        st.line_chart(HeightWeight_combine, use_container_width=True)
    elif option == 'Men & Women':
        st.text('Number of Men and Women of Medalist')
        st.line_chart(WomanMan_combine, use_container_width=True)
