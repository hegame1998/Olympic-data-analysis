# importing required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st

# creating the athletes dataset
athlete_df = pd.read_csv('https://raw.githubusercontent.com/MaH1996SdN/programming_project/master/athlete_events.csv')

# creating regions dataset
regions_df = pd.read_csv('https://raw.githubusercontent.com/MaH1996SdN/programming_project/master/noc_regions.csv')

# returning athletes dataset values
athlete_df

# returning regions dataset values
regions_df

# dropping extra column: note in regions dataframe
regions_df.drop('notes', axis=1, inplace=True)

regions_df.head(4)

# merging 2 datasets in order to find countries
athlete_df=pd.merge(athlete_df, regions_df, on='NOC', how='left')

athlete_df.head(4)

# renaming region to "Country" for better understanding
athlete_df.rename(columns = {'region':'Country'}, inplace = True)

athlete_df.head(4)

# dropping extra column: ID, Games, City, Team , Noc in athlete dataframe
athlete_df.drop(['ID','Team', 'NOC', 'Games', 'City'], axis=1, inplace=True)

athlete_df.head(4)

# counting the number of null values of dataset
print(athlete_df.isnull().sum())

# counting the number of null values of Medal column
athlete_df['Medal'].isnull().sum()

# counting the number of non-null values of Medal column
athlete_df['Medal'].notnull().sum()

# filling null values with "non-Medal"
athlete_df['Medal'].fillna('non-Medal', inplace = True)

# counting the number of null values of Medal column
athlete_df['Medal'].isnull().sum()

# Print values of Medal
print(athlete_df['Medal'])

# Print unique values of Medal
athlete_df["Medal"].unique()

# replacing string values of Medals with integer values
athlete_df.Medal.replace({'Gold':1, 'Silver':2, 'Bronze':3, 'non-Medal':0}, inplace=True)

# Print values of Medal
print(athlete_df['Medal'])

# Print unique values of Medal
athlete_df["Medal"].unique()

# getting information about each column counts and datatype in athlete dataframe
athlete_df.info()

# counting the number of null values of Country column
athlete_df['Country'].isnull().sum()

# counting the number of non-null values of Country column
athlete_df['Country'].notnull().sum()

# filling null values with "Unknown-Country"
athlete_df['Country'].fillna('Unknown-Country', inplace = True)

# counting the number of null values of Country column
athlete_df['Country'].isnull().sum()

# Print unique values of Country
athlete_df["Country"].unique()

# getting information about each column counts and datatype in athlete dataframe
athlete_df.info()

#Histogram of Age
athlete_df['Age'].hist()
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of Athlete Ages')
plt.show()

# counting the number of null values of Age column
athlete_df['Age'].isnull().sum()

# mean value of Age column
athlete_df['Age'].mean()

# filling null values with median of age
athlete_df['Age'].fillna(25, inplace = True)

# counting the number of null values of Age column after cleaning
athlete_df['Age'].isnull().sum()

#Histogram of Age
athlete_df['Age'].hist()
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of Athlete Ages')
plt.show()

#Histogram of Height
athlete_df['Height'].hist()
plt.xlabel('Height')
plt.ylabel('Frequency')
plt.title('Histogram of Athlete Height')
plt.show()

# counting the number of null values of Height column
athlete_df['Height'].isnull().sum()

# mean value of Height column
athlete_df['Height'].mean()

# filling null values of Height column with median value
athlete_df['Height'].fillna(athlete_df['Height'].mean(), inplace=True)

# counting the number of null values of Height column after cleaning
athlete_df['Height'].isnull().sum()

#Histogram of Height
athlete_df['Height'].hist()
plt.xlabel('Height')
plt.ylabel('Frequency')
plt.title('Histogram of Athlete Height')
plt.show()

#Histogram of Weight
athlete_df['Weight'].hist()
plt.xlabel('Weight')
plt.ylabel('Frequency')
plt.title('Histogram of Athlete Weight')
plt.show()

# counting the number of null values of Weight column
athlete_df['Weight'].isnull().sum()

# mean value of Weight column
athlete_df['Weight'].mean()

# filling null values of Weight column with median value
athlete_df['Weight'].fillna(athlete_df['Weight'].mean(), inplace=True)

# counting the number of null values of Weight column after cleaning
athlete_df['Weight'].isnull().sum()

#Histogram of Weight
athlete_df['Weight'].hist()
plt.xlabel('Weight')
plt.ylabel('Frequency')
plt.title('Histogram of Athlete Weight')
plt.show()

# counting the number of null values of dataset
print(athlete_df.isnull().sum())

athlete_df.info()
