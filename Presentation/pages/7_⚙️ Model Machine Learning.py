from loadData import  st,np,pd, athlete_df
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

st.set_page_config(
        page_title="⚙️ Model of Machine Learning",
        layout="wide",
    )
st.subheader("⚙️ Model of Machine Learning")
st.text('Please choose your method of machine learning or see the compare of methods.')


# defining function for changing string values to numeric values for better modeling
def encode_df(dataframe):
    le = LabelEncoder()
    for column in dataframe.columns:
        dataframe[column] = le.fit_transform(dataframe[column])
    return dataframe

athlete_df = encode_df(athlete_df)

# Select model
select_model = st.selectbox('Select Model :', ['DecisionTree', 'KNeighborsClassifier', 'RandomForestClassifier'])
if select_model == 'DecisionTree':
    model = DecisionTreeClassifier()
elif select_model == 'KNeighborsClassifier':
    model = KNeighborsClassifier()
else:
    model = RandomForestClassifier()

# Select features
features = st.multiselect('Select features',  ['Sex', 'Year', 'Medal', 'Height', 'Weight'])

# Test size slider
test_size = st.slider('Test size : ', min_value=0.1, max_value=0.9, step=0.1)

# Train model button
if st.button('Run Model'):
    if len(features) > 0:
        # Prepare data
        X = athlete_df.drop(features, axis=1)
        
        # Handle case where only one feature is selected
        if len(features) == 1:
            Y = athlete_df[features[0]]  # Select only one column as target variable
            Y = encode_df(pd.DataFrame(Y))  # Encode if it's a categorical variable
        else:
            # If multiple features are selected, choose the first one as the target variable
            st.warning('Multiple features selected. Using the first one as the target variable.')
            Y = athlete_df[features[0]]
            Y = encode_df(pd.DataFrame(Y))  # Encode if it's a categorical variable

        # Train-test split
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=42)
        
        # Train the model
        model.fit(X_train, Y_train)
        
        # Predictions
        Y_pred = model.predict(X_test)
        
        # Calculate accuracy
        accuracy = accuracy_score(Y_test, Y_pred)
        
        # Display accuracy
        st.write(f'Accuracy = {accuracy}')
    else:
        st.warning('Please select at least one feature.')