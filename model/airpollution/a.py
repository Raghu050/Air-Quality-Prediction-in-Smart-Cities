import json

# Read data from JSON file
with open('data.json') as f:
    data = json.load(f)
    districts_data = data["Karnataka"]["districts"]

# Now take district name as input from user
district_name = 'Bagalkot'

# Get district data
district = None
for d in districts_data:
    if d["name"].lower() == district_name.lower():
        district = d
        break

if district:
    print(f"Predicted values for {district_name} for the years 2025-2029:")
    for year in range(2025, 2030):
        print(f"Year {year}:")
        print(f"\tCO: {district['co'] + (year - 2025) * 0.01}")  # Incrementing CO by 0.01 each year
        print(f"\tNMHC: {district['nmhc'] + (year - 2025) * 0.005}")  # Incrementing NMHC by 0.005 each year
        print(f"\tC6H6: {district['c6h6'] + (year - 2025) * 0.003}")  # Incrementing C6H6 by 0.003 each year
        print(f"\tNO2: {district['no2'] + (year - 2025) * 0.002}")  # Incrementing NO2 by 0.002 each year
        print(f"\tTemperature: {district['temp'] + (year - 2025) * 0.1}")  # Incrementing Temperature by 0.1°C each year
        print(f"\tHumidity: {district['humidity'] - (year - 2025) * 1}")  # Decrementing Humidity by 1% each year
        print(f"\tPM2.5: {district['pm25'] - (year - 2025) * 1}")  # Decrementing PM2.5 by 1 µg/m³ each year
        print(f"\tSO2: {district['so2'] + (year - 2025) * 0.001}")  # Incrementing SO2 by 0.001 each year
        print(f"\tPM10: {district['pm10'] - (year - 2025) * 1.5}")  # Decrementing PM10 by 1.5 µg/m³ each year
        print(f"\tPM0.3: {district['pm03'] - (year - 2025) * 0.5}")  # Decrementing PM0.3 by 0.5 µg/m³ each year
else:
    print("District not found.")
