from loadData import pd, st

st.set_page_config(
        page_title="💾 Raw Dataset",
        layout="wide",
    )
st.subheader("💾 Raw dataset")
st.text('Please choose the dataset that you want to see below.')


#Tab of data showing
tab1, tab2 = st.tabs(["Dataset of Athletes", "Dataset of Countries"])
with tab1:
   # creating the athletes dataset
   athlete_df = pd.read_csv('https://raw.githubusercontent.com/MaH1996SdN/programming_project/master/athlete_events.csv')
   st.write('The raw dataset of Athlete of Olympic:')
   st.write(athlete_df)


with tab2:
   # creating regions dataset
   regions_df = pd.read_csv('https://raw.githubusercontent.com/MaH1996SdN/programming_project/master/noc_regions.csv')
   st.write('The raw dataset of Countries that participate in Olympic:')
   st.write(regions_df) 