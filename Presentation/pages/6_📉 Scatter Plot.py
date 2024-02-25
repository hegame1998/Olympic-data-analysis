from loadData import st,pd,np,sns, athlete_df

st.set_page_config(
        page_title="📈 Scatter Plot",
        layout="wide",
    )
st.subheader("📈 Scatter Plot")
st.text('Please select one item to see the Scatter Plot of athletes.')
st.text("Each point represents an athlete's age and height, with points colored based on the sex of the athlete.")

# Function to assign colors based on sex
def assign_color(sex):
    return 'Male' if sex == 'M' else 'Female'

# Assigning colors based on sex
athlete_df['Color'] = athlete_df['Sex'].apply(assign_color)

# Streamlit scatter chart
st.scatter_chart(
    athlete_df,
    x='Age',
    y='Height',
    color='Color',
    size=20,
    use_container_width=True
)


