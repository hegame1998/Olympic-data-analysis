import streamlit as st
import pandas as pd
import numpy as np


st.header("Presentation of Final Project")
st.subheader("Programming & Database")


val_count  = df['column_name'].value_counts()
fig = plt.figure(figsize=(10,5))
sns.barplot(val_count.index, val_count.values, alpha=0.8)
fig.title('Some title')
fig.ylabel('y label', fontsize=12)
fig.xlabel('x label', fontsize=12)


# Add figure in streamlit app
st.pyplot(fig)
