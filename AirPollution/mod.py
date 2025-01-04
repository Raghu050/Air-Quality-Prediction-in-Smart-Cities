# Import necessary libraries
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd

# Load historical pollution data
# Assuming 'pollution_data.csv' contains historical data with columns: 'District', 'Year', 'Pollution_Level'
pollution_data = pd.read_csv('pollution_data.csv')

# Filter data for years 2017-2023
historical_data = pollution_data[(pollution_data['Year'] >= 2017) & (pollution_data['Year'] <= 2023)]

# Prepare features (districts) and target variable (pollution levels)
X = historical_data['District']
y = historical_data['Pollution_Level']

# Encode districts using LabelEncoder
district_encoder = LabelEncoder()
X_encoded = district_encoder.fit_transform(X)

# Train Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_encoded.reshape(-1, 1), y)

# Define districts for 2024
districts_2024 = ['District A', 'District B', 'District C', ...]  # Add your districts here

# Encode districts for 2024 using LabelEncoder
districts_2024_encoded = district_encoder.transform(districts_2024)

# Make predictions for 2024
predictions_2024 = rf_model.predict(districts_2024_encoded.reshape(-1, 1))

# Convert predictions to dictionary format
recommendation_2024 = {district: round(pollution_level) for district, pollution_level in zip(districts_2024, predictions_2024)}

# Display recommendations
recommendation_2024
