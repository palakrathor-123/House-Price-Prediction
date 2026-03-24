import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import pickle
import os

# Paths setup (Aapki images ke mutabiq)
# house_prices.csv 'data' folder ke andar hai
csv_path = "data/house_prices.csv" 
model_save_path = "../model.pkl"
encoder_save_path = "../encoder.pkl"

try:
    df = pd.read_csv(csv_path)
    print("✅ Data Loaded successfully from data folder!")

    le = LabelEncoder()
    df['Location'] = le.fit_transform(df['Location'])

    X = df.drop('Price', axis=1)
    y = df['Price']

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Saving files in main directory
    with open(model_save_path, 'wb') as f:
        pickle.dump(model, f)
    with open(encoder_save_path, 'wb') as f:
        pickle.dump(le, f)

    print(f"🚀 Success! Files generated in main folder.")

except Exception as e:
    print(f"❌ Error: {e}")