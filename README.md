
# 🏠 House Price Prediction System

A full-stack Machine Learning application that predicts house prices based on features like area, bedrooms, and location. It includes a FastAPI backend and a Streamlit dashboard with interactive visualizations.

## 🚀 Features
* *Machine Learning:* Random Forest Regressor for price estimation.
* *API:* FastAPI for serving model predictions.
* *Dashboard:* Streamlit UI with Plotly charts (Scatter, Bar, Histogram).
* *Modular Structure:* Clean separation of data, source code, API, and UI.

## 🛠️ Tech Stack
* *Language:* Python
* *ML Libraries:* Pandas, Scikit-learn
* *API Framework:* FastAPI, Uvicorn
* *Frontend:* Streamlit, Plotly

## 📂 Project Structure
- data/: Contains house_prices.csv
- src/: Training script (train_model.py)
- api/: FastAPI server (main.py)
- ui/: Streamlit dashboard (app.py)
- model.pkl: Trained model file

## ⚙️ How to Run
1. *Train the Model:* python src/train_model.py
2. *Start API:* uvicorn api.main:app --reload
3. *Run Dashboard:* streamlit run ui/app.py

 ## Dashboard Preview
 <img width="1337" height="586" alt="Image" src="https://github.com/user-attachments/assets/547a0ef4-0781-4546-9c7c-8def7b53a825" />
