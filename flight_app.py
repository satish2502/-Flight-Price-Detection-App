import streamlit as st
import pandas as pd
import joblib

# --- Load dataset and model ---
df = pd.read_csv("flights_data.csv")
model = joblib.load('flight_price_model.pkl')

# --- App Title ---
st.title("✈️ Flight Price Prediction")
st.markdown("Predict the estimated flight price based on your travel details.")

# --- Sidebar for Inputs ---
st.sidebar.header("Enter Flight Details")

airline = st.sidebar.selectbox("Airline", df['airline'].unique())
source_city = st.sidebar.selectbox("Source City", df['source_city'].unique())
destination_city = st.sidebar.selectbox("Destination City", df['destination_city'].unique())
flight_class = st.sidebar.selectbox("Class", df['class'].unique())
stops = st.sidebar.selectbox("Stops", df['stops'].unique())
departure_time = st.sidebar.selectbox("Departure Time", df['departure_time'].unique())
arrival_time = st.sidebar.selectbox("Arrival Time", df['arrival_time'].unique())
duration = st.sidebar.number_input("Duration (hours)", min_value=0.0, max_value=30.0, step=0.5)
days_left = st.sidebar.number_input("Days left for travel", min_value=0, max_value=365, step=1)

# --- Create input dataframe ---
input_df = pd.DataFrame({
    'airline':[airline],
    'source_city':[source_city],
    'destination_city':[destination_city],
    'class':[flight_class],
    'stops':[stops],
    'departure_time':[departure_time],
    'arrival_time':[arrival_time],
    'duration':[duration],
    'days_left':[days_left]
})

# --- Predict Price ---
st.subheader("💰 Estimated Flight Price")
if st.button("Predict"):
    price = model.predict(input_df)[0]
    st.success(f"₹ {price:,.2f}")

# --- Optional: Show Input Summary ---
with st.expander("Show Entered Details"):
    st.write(input_df.T)
