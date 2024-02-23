import pandas as pd
import numpy as np
import seaborn as sns
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
import matplotlib.pyplot as plt
import streamlit as st


st.set_page_config(
        page_title="📊 Histogram",
        layout="wide",
    )

st.subheader("📊 Histogram")
st.text('Base on your choose you can see the plot below.')


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



# Data for histograms
athlete1_df = athlete_df['Age']
athlete2_df = athlete_df['Age'].fillna(athlete_df['Age'].mean())

athlete3_df = athlete_df['Height']
athlete4_df = athlete_df['Height'].fillna(athlete_df['Height'].mean())

athlete5_df = athlete_df['Weight']
athlete6_df = athlete_df['Weight'].fillna(athlete_df['Weight'].mean())

# Create tabs
tabs = ["Age", "Height", "Weight", "Sport"]
selected_tab = st.selectbox("Select Dataset", tabs)

# Display selected tab
if selected_tab == "Age":
    st.write("Histogram based on Age before the fill null cell and after it:")
    col1, col2 = st.columns(2)
    with col1:
        st.text("Before fill null cells")
        hist1, edges1 = np.histogram(athlete1_df.dropna(), bins=20)
        hist_df1 = pd.DataFrame({'Age': hist1, 'left': edges1[:-1], 'right': edges1[1:]})
        source1 = ColumnDataSource(hist_df1)
        p1 = figure(title='Histogram of Age', x_axis_label='Age', y_axis_label='Frequency')
        p1.quad(bottom=0, top='Age', left='left', right='right', source=source1, fill_color='blue', line_color='white', alpha=0.5)
        st.bokeh_chart(p1, use_container_width=True)
    
    with col2:
        st.text("After fill null cells")
        hist2, edges2 = np.histogram(athlete2_df.dropna(), bins=20)
        hist_df2 = pd.DataFrame({'Age': hist2, 'left': edges2[:-1], 'right': edges2[1:]})
        source2 = ColumnDataSource(hist_df2)
        p2 = figure(title='Histogram of Age (after fillna)', x_axis_label='Age', y_axis_label='Frequency')
        p2.quad(bottom=0, top='Age', left='left', right='right', source=source2, fill_color='green', line_color='white', alpha=0.5)
        st.bokeh_chart(p2, use_container_width=True)

elif selected_tab == "Height":
    st.write("Histogram based on Height before the fill null cell and after it:")
    col1, col2 = st.columns(2)
    with col1:
        st.text("Before fill null cells")
        hist3, edges3 = np.histogram(athlete3_df.dropna(), bins=20)
        hist_df3 = pd.DataFrame({'Height': hist3, 'left': edges3[:-1], 'right': edges3[1:]})
        source3 = ColumnDataSource(hist_df3)
        p3 = figure(title='Histogram of Height', x_axis_label='Height', y_axis_label='Frequency')
        p3.quad(bottom=0, top='Height', left='left', right='right', source=source3, fill_color='blue', line_color='white', alpha=0.5)
        st.bokeh_chart(p3, use_container_width=True)
    
    with col2:
        st.text("After fill null cells")
        hist4, edges4 = np.histogram(athlete4_df.dropna(), bins=20)
        hist_df4 = pd.DataFrame({'Height': hist4, 'left': edges4[:-1], 'right': edges4[1:]})
        source4 = ColumnDataSource(hist_df4)
        p4 = figure(title='Histogram of Height (after fillna)', x_axis_label='Height', y_axis_label='Frequency')
        p4.quad(bottom=0, top='Height', left='left', right='right', source=source4, fill_color='green', line_color='white', alpha=0.5)
        st.bokeh_chart(p4, use_container_width=True)

elif selected_tab == "Weight":
    st.write("Histogram based on Weight before the fill null cell and after it:")
    col1, col2 = st.columns(2)
    with col1:
        st.text("Before fill null cells")
        hist5, edges5 = np.histogram(athlete5_df.dropna(), bins=20)
        hist_df5 = pd.DataFrame({'Weight': hist5, 'left': edges5[:-1], 'right': edges5[1:]})
        source5 = ColumnDataSource(hist_df5)
        p5 = figure(title='Histogram of Weight', x_axis_label='Weight', y_axis_label='Frequency')
        p5.quad(bottom=0, top='Weight', left='left', right='right', source=source5, fill_color='blue', line_color='white', alpha=0.5)
        st.bokeh_chart(p5, use_container_width=True)
    
    with col2:
        st.text("After fill null cells")
        hist6, edges6 = np.histogram(athlete6_df.dropna(), bins=20)
        hist_df6 = pd.DataFrame({'Weight': hist6, 'left': edges6[:-1], 'right': edges6[1:]})
        source6 = ColumnDataSource(hist_df6)
        p6 = figure(title='Histogram of Weight (after fillna)', x_axis_label='Weight', y_axis_label='Frequency')
        p6.quad(bottom=0, top='Weight', left='left', right='right', source=source6, fill_color='green', line_color='white', alpha=0.5)
        st.bokeh_chart(p6, use_container_width=True)

elif selected_tab == "Sport":
    st.write("Histogram based on athletes who win gold medal that over 50 base on sport:")
    # Filter athletes older than 50
    GoldMedal = athlete_df.loc[athlete_df['Medal'] == 1]
    filtered_df = GoldMedal[GoldMedal['Age'] > 50]
    sport_counts = filtered_df['Sport'].value_counts()
    p = figure(
        title='Athletes Over 50 by Sport',
        x_axis_label='Sport',
        y_axis_label='Count',
        x_range=list(sport_counts.index),  # Set x-axis range to sports
        plot_height=400, 
        plot_width=700
    )
    p.vbar(
        x=list(sport_counts.index), 
        top=sport_counts.values, 
        width=0.5,
        fill_color='green'
    )
    p.xaxis.major_label_orientation = "vertical"
    st.bokeh_chart(p, use_container_width=True)