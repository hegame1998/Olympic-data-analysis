from loadData import pd,np, sns, plt, st, athlete_df

st.set_page_config(
        page_title="🥧 Pie chart",
        layout="wide",
    )
st.subheader("🥧 Pie chart")
st.text('Base on your choose can see the pie chart of dataset.')


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

