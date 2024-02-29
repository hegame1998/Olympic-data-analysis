from loadData import athlete_df, pd, np, sns, plt, st

st.set_page_config(
        page_title="📏 Correlation",
        layout="wide",
    )
st.subheader("📏 Correlation")
st.text('Please choose the dataset that you want to see below.')


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
        options=["Correlation Matrix", "Heatmap"],
    )

with col2:
    if st.session_state.display_option == "Correlation Matrix":
        st.write("Correlation of data:")
        st.write(correlation_matrix)
    elif st.session_state.display_option == "Heatmap":
        st.write("Heatmap of data:")
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
        st.pyplot(fig)
    



