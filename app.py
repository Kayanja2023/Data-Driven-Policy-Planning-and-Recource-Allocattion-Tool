# Import necessary libraries
import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import tweepy

# Function to predict next year's crime count
def predict_crime_count(model, current_year_count):
    return model.predict([[current_year_count]])[0]

# Function to plot prediction
def plot_prediction(current, prediction):
    fig, ax = plt.subplots(figsize=(10, 6))
    years = ['Current Year', 'Next Year']
    counts = [current, prediction]
    ax.barh(years, counts, color=['blue', 'green'])
    ax.set_xlabel('Crime Count')
    ax.set_title('Crime Count Prediction')
    for i, v in enumerate(counts):
        ax.text(v, i, str(int(v)))
    st.pyplot(fig)

# Initialize the Streamlit app
st.title("Crime Prediction Dashboard for Mdantsane, South Africa")

# Sidebar for additional inputs and information
st.sidebar.header("Additional Information")
st.sidebar.write("This dashboard predicts the crime count for the next year based on the current year's data.")
st.sidebar.write("Select the type of crime to get specific policy recommendations.")

# User input for the type of crime
crime_type = st.sidebar.selectbox("Type of Crime", ["Violent Crime", "Property Crime", "Drug-related Crime", "Other"])

# User input for the current year's crime count
current_year_count = st.number_input("Enter the crime count for the current year:", min_value=0)

# Dummy model for demonstration (Replace this with your trained model)
model = LinearRegression()
model.coef_ = np.array([1.02])
model.intercept_ = 5

# Predict the crime count for the next year
next_year_prediction = predict_crime_count(model, current_year_count)

# Display the prediction
st.subheader(f"Predicted crime count for next year: {int(next_year_prediction)}")

# Plot the prediction
plot_prediction(current_year_count, next_year_prediction)

# Display sentiment analysis (Hypothetical)
st.subheader("Sentiment Analysis from Twitter Data")
st.write("Positive: 40%")
st.write("Neutral: 35%")
st.write("Negative: 25%")

# Display relevant news articles based on the type of crime
st.subheader("Relevant News Articles")
if crime_type == "Drug-related Crime":
    st.markdown("""
    - [New data show US drug epidemic is deadlier than ever](https://www.cnn.com/2022/02/16/health/drug-overdose-deaths-record-high/index.html)
    - [Drug Arrests Stayed High Even as Imprisonment Fell](https://www.pewtrusts.org/en/research-and-analysis/issue-briefs/2022/02/drug-arrests-stayed-high-even-as-imprisonment-fell-from-2009-to-2019)
    """)
elif crime_type == "Property Crime":
    st.markdown("""
    - [Angry Mdantsane residents confront alleged cable thieves](https://www.news24.com/news24/southafrica/news/angry-mdantsane-residents-confront-alleged-cable-thieves-20230121)
    - [Mdantsane community crime fighters arrested](https://www.dispatchlive.co.za/news/2021-08-26-mdantsane-community-crime-fighters-arrested/)
    """)
else:
    st.markdown("""
    - [Residents praise Mdantsane Crime Forum's progress](https://www.pressreader.com/south-africa/daily-dispatch/20220328/282067690439803)
    - [Mdantsane residents come out in support of vigilantism accused](https://www.groundup.org.za/article/forum-members-gone-into-hiding-after-accusing-police-of-trying-to-silence-them-for-exposing-police-failures-in-mdantsane/)
    """)

# To run the app, save this code in a file named 'app.py'
# Open a terminal, navigate to the folder containing 'app.py', and run 'streamlit run app.py'

# Authenticate to Twitter
auth = tweepy.OAuthHandler("X4x4k70DB7LGbBCQ49yrLVdIu", "U3JpJIYNSJ0XA48qtk3zCxe0bWTcK7e2Dr3A62v8K6aXMVc8hb")
auth.set_access_token("1706198531743121408-EzJa4ON1JXmSaNg8y4MlMWePja7u24", "eMMXWAV22J6ScYC039ltSshkEpxrmR5g4ntxv4MuDPeXo")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)

# Fetch tweets
tweets = api.search(q="Mdantsane crime", lang="en", count=10)

for tweet in tweets:
    print(f"{tweet.user.name} said {tweet.text}")
