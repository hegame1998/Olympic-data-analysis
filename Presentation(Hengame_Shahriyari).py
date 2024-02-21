# **Importing the modules & libraries**

# importing required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st

# **Data Importing**

I called the data from the main source (GitHub) and put them in a specific variable to use it in future analysis.

# creating the athletes dataset
athlete_df = pd.read_csv('https://raw.githubusercontent.com/MaH1996SdN/programming_project/master/athlete_events.csv')

# creating regions dataset
regions_df = pd.read_csv('https://raw.githubusercontent.com/MaH1996SdN/programming_project/master/noc_regions.csv')

# **Information about dataset**


# returning athletes dataset values
athlete_df

In previous code, at the end of dataset we can see the size of data (number of rows and columns) but we can see it with another code :

# returning the number of rows and columns in athletes dataset
athlete_df.shape

This method is used to retrieve the first few rows of the dataset. <br>It returns 5 rows by default, but we can call for specific rows. <br>We call 8 rows here, so it will return the first 8 rows of the dataset.

# returning first n rows of athletes dataset
athlete_df.head(8)

This code same as last code but print the last rows of dataset

# returning last n rows of athletes dataset
athlete_df.tail(3)

This method provides a concise summary of the dataset's information, including the number of non-null entries and the data types of each column.<br>This is useful for understanding the data types in dataset and identifying any missing values so we can clean the data if there is any empty cell.

# getting information about each column counts and datatype in athlete dataframe
athlete_df.info()

This method is used to generate descriptive statistics of the data. <br>For a dataset, it provides a summary of the central tendency, dispersion, and shape of the distribution of the data. For each numeric column in the dataset, it calculates statistics such as count, mean, standard deviation, minimum, 25th percentile, median (50th percentile), 75th percentile, and maximum.

# getting information like min,max and mean about numeric columns in athlete dataframe
athlete_df.describe()

Repeat previous code for this dataset


# returning regions dataset values
regions_df

# returning the number of rows and columns in athletes dataset
regions_df.shape

# getting information about each column counts and datatype in region dataframe
regions_df.info()

# getting information like min,max and mean about numeric columns in region dataframe
regions_df.describe()

# **Drop & Merge dataset**

Remove a column named 'notes'. <br> The **axis=1** parameter specifies that you're dropping a column but if it is 0, refers to row, and **inplace=True** means that the change will be applied directly to the original dataset instead of creating a new one.

# dropping extra column: note in regions dataframe
regions_df.drop('notes', axis=1, inplace=True)

regions_df.head(4)

We can now join the two dataframes using as key the NOC column with the Pandas **'Merge'** function

# merging 2 datasets in order to find countries
athlete_df=pd.merge(athlete_df, regions_df, on='NOC', how='left')

athlete_df.head(4)

Change the tag of region column to country

# renaming region to "Country" for better understanding
athlete_df.rename(columns = {'region':'Country'}, inplace = True)

athlete_df.head(4)

Now I want to delete the columns that are extra in the dataset and we do not need them for future analyse.

# dropping extra column: ID, Games, City, Team , Noc in athlete dataframe
athlete_df.drop(['ID','Team', 'NOC', 'Games', 'City'], axis=1, inplace=True)

athlete_df.head(4)

# **Cleaning dataset**

Cleaning the dataset before analysis is a fundamental step to ensuring the quality, reliability, and integrity of results. It allows for a perfect analysis and helps in drawing accurate and meaningful conclusions.


### **Calculate null cells**

I calculate the number of null cells.

# counting the number of null values of dataset
print(athlete_df.isnull().sum())

We can see that Age, Height, Weight, Medal and Country have a lot of missing values. <br>
Always we should start with the least amount of value, but here Medals have NaN in about 231333 rows and this can be explained since not all participating athletes would win medals. <br>
Let's replace these missing values with 'non-Medal'.

### **Cleaning base on *'Medal'***

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

Now I want to see the different type of medal that is in the dataset

# Print unique values of Medal
athlete_df["Medal"].unique()

Now I want to change the type of medal from **string** to **integer** so I will change them base on this : <br>
**Gold=1** , **Silver=2** , **Bronze=3** , **non-Medal=0**

# replacing string values of Medals with integer values
athlete_df.Medal.replace({'Gold':1, 'Silver':2, 'Bronze':3, 'non-Medal':0}, inplace=True)

# Print values of Medal
print(athlete_df['Medal'])

# Print unique values of Medal
athlete_df["Medal"].unique()

# getting information about each column counts and datatype in athlete dataframe
athlete_df.info()

Now I should continue with other values. <br> First, I should clean the value that is less than others, so cleaning should be based on this list:

1.   Country
2.   Age
3.   Height
4. Weight      



### **Cleaning base on *'Country'***

# counting the number of null values of Country column
athlete_df['Country'].isnull().sum()

# counting the number of non-null values of Country column
athlete_df['Country'].notnull().sum()

# filling null values with "Unknown-Country"
athlete_df['Country'].fillna('Unknown-Country', inplace = True)

# counting the number of null values of Country column
athlete_df['Country'].isnull().sum()

Now I want to see the different type of country that is in the dataset

# Print unique values of Country
athlete_df["Country"].unique()

# getting information about each column counts and datatype in athlete dataframe
athlete_df.info()

### **Cleaning base on *'Age'***

First of all I print the histogram of Age, I use the **hist()** function that is provided by pandas. <br> I show label for X and Y and show a label for histogram. <br> When I clean the null cells of Age, I will print this histogram again.

#Histogram of Age
athlete_df['Age'].hist()
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of Athlete Ages')
plt.show()

# counting the number of null values of Age column
athlete_df['Age'].isnull().sum()

The number of null value of age is around 9500 and I fill it with median of age so first I calculate median of age:

# mean value of Age column
athlete_df['Age'].mean()

then fill the **nan** value with median of Age.

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

### **Cleaning base on *'Height'***

Here I will repeat the levels of Age for **Height**.

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

### **Cleaning base on *'Weight'***

Here I will repeat the levels of Age for **Weight**.

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

Now this dataset is clear, without any null cells, and we can do analysis on it.

# **Exploration on clean dataset**

Now I explore the dataset again that I cleaned.

# returning the number of rows and columns in athletes dataset that cleaning
athlete_df.shape

# returning first n rows of athletes dataset
athlete_df.head(4)

# returning last n rows of athletes dataset
athlete_df.tail(3)

# getting information about each column counts and datatype in athlete dataframe
athlete_df.info()

# getting information like min,max and mean about numeric columns in athlete dataframe
athlete_df.describe()

This is a pandas dataset method used to compute pair correlation of columns, excluding null values. <br> It computes the correlation matrix for the numerical columns in the DataFrame so it shows just **Age**, **Height**, **Weight**, **Year**, **Medal**.

# finding correlation between different feaures
athlete_df.corr()

### **Explore about Medal**

I want to explore about **Non Medal**, we filled the null cell for medal with 0 so will calculate it in dataset.

# number of gold medals
athlete_df['Medal'].value_counts()[0]

I want to explore about **Gold Medal**, we filled the gold medal with 1 so will calculate it in dataset.

# number of gold medals
athlete_df['Medal'].value_counts()[1]

I want to explore about **Silver Medal**, we filled the silver medal with 2 so will calculate it in dataset.

# number of silver medals
athlete_df['Medal'].value_counts()[2]

I want to explore about **Bronze Medal**, we filled the bronze medal with 3 so will calculate it in dataset.

# number of Bronze medals
athlete_df['Medal'].value_counts()[3]

Sum of all type of medals. <br> I save the data that has medal (Gold, Silver, Bronze) in **Medals** data to use it in the future.

# number of all medals
Medals = athlete_df.loc[athlete_df['Medal'] != 0 ]
Medals.shape[0]

Display the list of the first and last countries based on the number of their medals so I should use **Medals** data

# top 5 countries with medals
Medals.Country.value_counts().head(5)

# last 5 countries with medals
Medals.Country.value_counts().tail(5)

I want to show the sports that has medal separately based on their type so I should use **Medals** dataset

# top 20 sports with medals
Medals.Sport.value_counts().head(20)

# last 20 sports with medals
Medals.Sport.value_counts().tail(20)

Now I want to explore in medal base on **gold** type so I save it in **GoldMedal** and use it in future detect. <br> At the first I list the first and last 5 countries that receive gold medal:

# top 5 countries with gold medals
GoldMedal = athlete_df.loc[athlete_df['Medal'] == 1]
GoldMedal.Country.value_counts().head(5)

# last 5 countries with gold medals
GoldMedal.Country.value_counts().tail(5)

I want to show the sports that has gold medal separately based on their type so I use **GoldMedal** dataset

# top 20 sports with gold medals
GoldMedal.Sport.value_counts().head(20)

# last 20 sports with gold medals
GoldMedal.Sport.value_counts().tail(20)

### **Explore about Woman Athlete**

Count the womans that participate in Olympic in 10 first countries:

# number of Womans
athlete_df['Sex'].value_counts()['F']

Now I should put the woman athletes in a dataset (**WomanAthlete**) and use it and show the 10 top country:

# number of woman athlete by country / top 10
WomanAthlete = athlete_df.loc[(athlete_df['Sex'] == 'F')]

WomanAthlete.Country.value_counts().head(10)

# number of woman athlete by country / last 10
WomanAthlete.Country.value_counts().tail(10)

Now I want to explore in woman who win medal so calculate it and put it in a dataset (**WomanMedalist**):

# number of woman medalists
WomanMedalist = WomanAthlete.loc[WomanAthlete['Medal'] != 0]
WomanMedalist.shape[0]

# number of woman medalists by country / top 5
WomanMedalist.Country.value_counts().head(5)

# number of woman medalists by country / last 5
WomanMedalist.Country.value_counts().tail(5)

# number of female medalists by sport / top 5
WomanMedalist.Sport.value_counts().head(5)

#**Visualization**

# correlation graph
plt.figure(figsize=(6,5))
sns.heatmap(athlete_df.corr(), annot=True)
plt.title('correlation', fontweight='bold', fontsize=14)
plt.show()

Pie chart for gender of dataset:

# athletes by sex
labels = ['Male', 'Female']
plt.figure(figsize=(10,6))
plt.pie(athlete_df['Sex'].value_counts(), labels=labels, autopct='%.2f%%')
plt.title('Percentage of athletes by sex', fontweight='bold', fontsize=14)
plt.legend()
plt.show()

The athletes over 50 years:

# athletes over 50 base on sport
plt.figure(figsize=(10, 5))
plt.tight_layout()
sns.countplot(x=GoldMedal['Sport'][GoldMedal['Age'] > 50],  palette='muted')
plt.title('Gold Medals for Athletes Over 50')
plt.xticks(rotation = 50)
plt.show()

# top 10 countries with medals
TotalMedal = Medals.Country.value_counts().reset_index(name='Medal').head(10)
ax = sns.catplot(x="index", y="Medal", data=TotalMedal, height=6, kind="bar", palette='hsv')
ax.set_xlabels('Countries', fontsize=12 )
ax.set_ylabels('Number of Medals', fontsize=12)
plt.title('Top 10 countries by number of medals', fontweight='bold', fontsize=14)
plt.xticks(rotation = 45)
plt.show()

# top 10 countries with Woman medalists
WomanMedalistByCountry = WomanMedalist.Country.value_counts().reset_index(name='Medal').head(15)
ax = sns.catplot(x='index', y='Medal', data=WomanMedalistByCountry, height=6, kind='bar', palette='Blues')
ax.set_xlabels('Countries' , fontsize=12 )
ax.set_ylabels('Number of Medals', fontsize=12)
plt.title('Top 10 countries with female medalists', fontweight='bold', fontsize=14)
plt.xticks(rotation = 45)
plt.show()

# athletes of Italy win gold medal came from Italy
plt.figure(figsize=(10, 5))
plt.tight_layout()
sns.countplot(x=GoldMedal['Year'][GoldMedal['Country'] == 'Italy'],  palette='Greens')
plt.title('Gold Medals for Athletes of Italy')
plt.xticks(rotation = 50, fontsize=8)
plt.show()

# Height of medalists
plt.figure(figsize=(10,6))
plt.plot(Medals['Height'].value_counts().sort_index())
plt.xticks(np.arange(130, 230, step=5))
plt.title('Height of medalists', fontweight='bold', fontsize=14)
plt.xlabel('Height', fontsize=12)
plt.show()

This code is using the seaborn library to create a scatter plot to visualize the relationship between two variables: age and height.<br>
Each point represents an athlete's age and height, with points colored based on the sex of the athlete.

# Create a scatter plot to visualize the relationship between age and height of athletes,
sns.scatterplot(x='Age', y='Height', hue='Sex', data=athlete_df , palette='Blues')
plt.title('Age vs. Height')

sns.pairplot(athlete_df,vars=['Sex','Age','Year','Medal'])

# **Modelling**

Call the library for machine learning:

# importing required tools from sklearn library
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

**Creating Training Set and Test Set for Models** <br>
We need to extract a sub dataframe with the features and the correct label.<br>
So I deleted some features and save in another dataset.





So I change the data of object to integer. <br>
I cheanged that an athlete is a male to 1 otherwise 0, same for season, summer is labeled as 1 and winter as 0.<br>
The test set size is 20% of the whole dataset. <br>

# defining function for changing string values to numeric values for better modelling
def encode_df(dataframe):
    le = LabelEncoder()
    for column in dataframe.columns:
        dataframe[column] = le.fit_transform(dataframe[column])
    return dataframe

# removing extra features which do not affect prediction containing "Event"
athlete_df2 = athlete_df.drop(['Name', 'Season','Country', 'Sport'], axis=1)

# changing string values to numeric values
encode_df(athlete_df2)

 #removing extra features which do not affect prediction without "Event" and "Sport"
athlete_df3 = athlete_df.drop(['Name', 'Season','Country', 'Event', 'Sport'], axis=1)

# changing string values to numeric values
encode_df(athlete_df3)

# defining prediction base on medal achievements
Y_medal = athlete_df2['Medal']
X_medal = athlete_df2.drop(['Medal'], axis=1)

Y_medal = athlete_df3['Medal']
X_medal = athlete_df3.drop(['Medal'], axis=1)

# defining train and test set data
X_train, X_test, Y_train, Y_test = train_test_split(X_medal, Y_medal, test_size=0.2, random_state=42)

### **Model 1 - Decision Tree**

# Call decision tree
model_decisionTree = DecisionTreeClassifier()

**Training Set**

# Train the dataset
model_decisionTree = model_decisionTree.fit(X_train, Y_train)

**Testing set**

# Test the dataset and print accuracy
Y_predict = model_decisionTree.predict(X_test)
ac_decisionTree = accuracy_score(Y_test, Y_predict)
print(ac_decisionTree)

### **Model 2 - KNeighborsClassifier**

# Call KNeighborsClassifier
model_KNeighbor = KNeighborsClassifier()

**Training Set**

# Train the dataset
model_KNeighbor = model_KNeighbor.fit(X_train, Y_train)

**Testing set**

# Test the dataset and print accuracy
Y_predict = model_KNeighbor.predict(X_test)
ac_KNeighborsClassifier = accuracy_score(Y_test, Y_predict)
print(ac_KNeighborsClassifier)

### **Model 3 - RandomForestClassifier**

# Call RandomForestClassifier
model_RandomForest = RandomForestClassifier()

**Training Set**

# Train the dataset
model_RandomForest = model_RandomForest.fit(X_train, Y_train)

**Testing set**

# Test the dataset and print accuracy
Y_predict = model_RandomForest.predict(X_test)
ac_RandomForestClassifier = accuracy_score(Y_test, Y_predict)
print(ac_RandomForestClassifier)

### **Compare different Models**

#Print all accuracy score of models
print('accuraaccuracy of Decision Tree model:', ac_decisionTree)
print('accuraaccuracy of k-nearest neighbors model:', ac_KNeighborsClassifier)
print('accuraaccuracy of Random Forest Classifier model:', ac_RandomForestClassifier)

The accuracy scores are typically values between 0 and 1, where higher values indicate better performance.

so we can see results of 3 methods are so close to each other but the method of **k-nearest neighbors** is a bit better than other.
