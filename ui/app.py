import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(page_title="House Price Dashboard", layout="wide")
st.title("🏠 House Price Prediction & Analysis")

# Sidebar for Prediction
st.sidebar.header("Enter Details")
area = st.sidebar.number_input("Area (sqft)", value=1500)
beds = st.sidebar.number_input("Bedrooms", value=3)
baths = st.sidebar.number_input("Bathrooms", value=2)
loc = st.sidebar.selectbox("Location", ["Suburb", "City_Center", "Rural", "Luxury_Hub"])
age = st.sidebar.number_input("Age (Years)", value=5)

if st.sidebar.button("Predict Price"):
    try:
        payload = {"area": area, "bedrooms": beds, "bathrooms": baths, "location": loc, "age": age}
        res = requests.post("http://127.0.0.1:8000/predict", json=payload)
        st.sidebar.success(f"Predicted Price: ₹{res.json()['predicted_price']}")
    except:
        st.sidebar.error("API is not running!")

# --- Visualizations (Data is in ../data/ folder) ---
df = pd.read_csv('data/house_prices.csv')

c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("Price vs Area")
    fig1 = px.scatter(df, x="Area_sqft", y="Price", color="Location")
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    st.subheader("Location Distribution")
    fig2 = px.bar(df, x="Location", y="Price", color="Location")
    st.plotly_chart(fig2, use_container_width=True)

with c3:
    st.subheader("Price Range")
    fig3 = px.histogram(df, x="Price")
    st.plotly_chart(fig3, use_container_width=True)