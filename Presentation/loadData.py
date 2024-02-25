import pandas as pd
import numpy as np
import seaborn as sns
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
import matplotlib.pyplot as plt
import streamlit as st


# datasets
athlete_df = pd.read_csv('https://raw.githubusercontent.com/MaH1996SdN/programming_project/master/athlete_events.csv')
athleteRaw_df = pd.read_csv('https://raw.githubusercontent.com/MaH1996SdN/programming_project/master/athlete_events.csv')
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


# Data for histograms
athlete1_df = athleteRaw_df['Age']
athlete2_df = athlete_df['Age'].fillna(athlete_df['Age'].mean())

athlete3_df = athleteRaw_df['Height']
athlete4_df = athlete_df['Height'].fillna(athleteRaw_df['Height'].mean())

athlete5_df = athleteRaw_df['Weight']
athlete6_df = athlete_df['Weight'].fillna(athleteRaw_df['Weight'].mean())

Medals = athlete_df.loc[athlete_df['Medal'] != 0]
# return athlete_df