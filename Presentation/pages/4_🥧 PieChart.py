import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(
        page_title="🥧 Pie chart",
        layout="wide",
    )

st.subheader("🥧 Pie chart")
st.text('Base on your choose can see the pie chart of dataset.')


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



# Function to create pie chart based on selected feature
def create_pie_chart(feature):
    labels = athlete_df[feature].value_counts().index.tolist()
    sizes = athlete_df[feature].value_counts().tolist()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(sizes, labels=labels, autopct='%.2f%%')
    ax.set_title(f'Percentage of athletes by {feature}', fontweight='bold', fontsize=14)
    ax.legend()
    st.pyplot(fig)
    
# Layout
left_column, right_column, empty = st.columns([1, 2, 2])

with left_column:
    feature = st.radio('Feature', ['Sex', 'Medal', 'Season'])
    

with right_column:
    create_pie_chart(feature)
    st.caption(f'Pie Chart based on {feature}')

