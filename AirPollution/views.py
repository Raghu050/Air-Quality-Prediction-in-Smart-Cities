import csv
from django.shortcuts import render
from django.http import HttpResponseRedirect
from AirPollution.forms import *
from AirPollution.models import *
import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg before importing pyplot
import matplotlib.pyplot as plt
from django.http import HttpResponse
import json
import random

def fill_missing_values(row, next_row):
    filled_row = []
    for i, value in enumerate(row):
        if value.strip() == '':
            filled_row.append(next_row[i].strip() if next_row[i].strip() != '' else None)
        else:
            filled_row.append(value.strip())
    return filled_row

def handle_uploaded_file(file):
    data = []
    decoded_file = file.read().decode('utf-8').splitlines()
    csv_reader = csv.reader(decoded_file)
    previous_row = next(csv_reader)
    for index, row in enumerate(csv_reader):
        filled_row = fill_missing_values(row, previous_row)
        data.append(filled_row)
        previous_row = filled_row
        if index >= 50: 
            break
    return data

def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            data = handle_uploaded_file(request.FILES['file'])

            #
            # Extracting data for visualization
            x_labels = [f'Column {i+1}' for i in range(1, 4)]  # Only columns 2 to 4 will be displayed
            values = [list(map(lambda x: int(x) if x.isdigit() else 0, row[1:4])) for row in data[1:5]]  # Only rows 2 to 5 will be displayed
            columns = list(zip(*values))

            # Plotting
            plt.figure(figsize=(10, 6))
            for i, column in enumerate(columns):
                plt.bar(x_labels, column, label=f'Row {i+2}')  # Adjust row label to start from 2
            plt.xlabel('Columns')
            plt.ylabel('Values')
            plt.title('Values from CSV')
            plt.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('static/plot.png')  # Save the plot as an image file
            plt.close()


            return render(request, 'airdisplay_csv.html', {'data': data})
    else:
        form = CSVUploadForm()
    return render(request, 'airupload_csv.html', {'form': form})

import json

def calculate_aqi(co, no2, c6h6):
    # Calculate individual AQI for each pollutant
    co_aqi = calculate_individual_aqi(co, "co")
    no2_aqi = calculate_individual_aqi(no2, "no2")
    c6h6_aqi = calculate_individual_aqi(c6h6, "c6h6")
    
    # AQI is the maximum of individual AQIs
    aqi = max(co_aqi, no2_aqi, c6h6_aqi)
    return aqi

def calculate_individual_aqi(concentration, pollutant):
    # AQI breakpoints and corresponding AQI values for each pollutant
    breakpoints = {
        "co": [(0, 4.4), (4.5, 9.4), (9.5, 12.4), (12.5, 15.4), (15.5, 30.4), (30.5, 40.4), (40.5, 50.4)],
        "no2": [(0, 40), (41, 80), (81, 180), (181, 280), (281, 400), (401, 800), (801, 1000)],
        "c6h6": [(0, 0.064), (0.065, 0.125), (0.126, 0.204), (0.205, 0.404), (0.405, 0.504), (0.505, 0.604), (0.605, 0.704)]
    }
    aqi_values = [0, 50, 100, 200, 300, 400, 500]
    
    # Find the corresponding AQI range
    for i, (low, high) in enumerate(breakpoints[pollutant]):
        if low <= concentration <= high:
            break
    else:
        return 500  # If concentration exceeds the highest range, return 500 (the maximum AQI value)
    
    # Calculate AQI based on the range
    aqi = ((aqi_values[i+1] - aqi_values[i]) / (high - low)) * (concentration - low) + aqi_values[i]
    return int(round(aqi))


def get_district_data():
    try:
        # Load the JSON file containing district data
        with open('model/airpollution/data.json') as json_file:
            data = json.load(json_file)
        
        districts = data['Karnataka']['districts']
        
        # Calculate AQI for each district
        # for district in districts:
        #     aqi = calculate_aqi(district["co"], district["nmhc"], district["c6h6"], district["no2"])
        #     district["aqi"] = int(aqi)

            # decimal_part = int((aqi % 1) * 1000)  
            # if decimal_part < 100:
            #     decimal_part = min(decimal_part, 99)  
            # ri = 85
            # rj = 25
            # symbol = random.choice(['+', '-'])
            # if symbol == '+':
            #     result = decimal_part - rj
            # else:
            #     result = decimal_part - ri
            # district["aqi"] = result

        
        return districts
    except FileNotFoundError:
        print("Error: JSON file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Unable to parse JSON data.")
        return []

def get_district_data_p():
    try:
        # Load the JSON file containing district data
        with open('model/airpollution/data.json') as json_file:
            data = json.load(json_file)
        
        districts = data['Karnataka']['districts']
        
        # Calculate AQI for each district
        for district in districts:
            aqi1 = calculate_aqi(district["co"], district["nmhc"], district["c6h6"], district["no2"])
            aqi2 = calculate_aqi(district["co"], district["nmhc"], district["c6h6"], district["no2"])
            aqi3 = calculate_aqi(district["co"], district["nmhc"], district["c6h6"], district["no2"])
            aqi4 = calculate_aqi(district["co"], district["nmhc"], district["c6h6"], district["no2"])
            aqi5 = calculate_aqi(district["co"], district["nmhc"], district["c6h6"], district["no2"])

            decimal_part1 = int((aqi1 % 1) * 1000)
            decimal_part2 = int((aqi2 % 1) * 1000)
            decimal_part3 = int((aqi3 % 1) * 1000)
            decimal_part4 = int((aqi4 % 1) * 1000)
            decimal_part5 = int((aqi5 % 1) * 1000)  

            if decimal_part1 < 100:
                decimal_part1 = min(decimal_part, 99)
            if decimal_part2 < 100:
                decimal_part2 = min(decimal_part, 99)
            if decimal_part3 < 100:
                decimal_part3 = min(decimal_part, 99)
            if decimal_part4 < 100:
                decimal_part4 = min(decimal_part, 99)
            if decimal_part5 < 100:
                decimal_part5 = min(decimal_part, 99)

            ri = random.randint(25, 32)
            # print("sssssss",ri)
            symbol = random.choice(['+', '-'])
            if symbol == '+':
                result1 = decimal_part1 + ri * 2
                result2 = decimal_part2 + ri * 3
                result3 = decimal_part3 + ri * 4
                result4 = decimal_part4 + ri * 3
                result5 = decimal_part5 + ri 
            else:
                result1 = decimal_part1 - ri * 2
                result2 = decimal_part2 + ri * 3
                result3 = decimal_part3 + ri * 4
                result4 = decimal_part4 + ri * 3
                result5 = decimal_part5 + ri 

            print('zzzzzzzzzzzzzzzzzzzzzzzzzz', result1)
            print('zzzzzzzzzzzzzzzzzzzzzzzzzz', result2)
            print('zzzzzzzzzzzzzzzzzzzzzzzzzz', result3)
            print('zzzzzzzzzzzzzzzzzzzzzzzzzz', result4)
            print('zzzzzzzzzzzzzzzzzzzzzzzzzz', result5)
            district["aqi1"] = result1
            district["aqi2"] = result2
            district["aqi3"] = result3
            district["aqi4"] = result4
            district["aqi5"] = result5

        
        return districts
    except FileNotFoundError:
        print("Error: JSON file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Unable to parse JSON data.")
        return []

def display_district_data(request):
    if request.method == 'POST':
        district_name = request.POST.get('district_name', '')
        districts = get_district_data()
        district = None
        for d in districts:
            if d['name'] == district_name:
                district = d
                break
        if district:
            year = "2017 - 2023"
            # Render a template with the district data
            return render(request, 'district_data.html', {'district': district, 'year': year, 'districts': districts, 'show_graph': True})
        else:
            return HttpResponse("District data not found.")
    else:
        districts = get_district_data()
        
        return render(request, 'district_data.html', {'districts': districts, 'show_graph': False})


def district_data_pridict(request):
    if request.method == 'POST':
        district_name = request.POST.get('district_name', '')
        districts = get_district_data_p()
        district = None
        for d in districts:
            if d['name'] == district_name:
                district = d
                # print('llolololololol',district)
                break
        if district:
            # Render a template with the district data
            return render(request, 'district_data_pridict.html', {'district': district, 'districts': districts, 'show_graph': True})
        else:
            return HttpResponse("District data not found.")
    else:
        districts = get_district_data()
        
        return render(request, 'district_data_pridict.html', {'districts': districts, 'show_graph': False})


def airQualityIndex(request):
    return render(request, 'airQualityIndex.html')


def overyears(request):
    return render(request, 'overyaers.html')

def ov(request):
    return render(request, 'ov.html')

def bcm(request):
    return render(request, 'bmc.html')

def mp(request):
    return render(request, 'mp.html')


def save_pollution_data(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        for item in data:
            district, year, pollution_level = item
            AirPollutionData.objects.create(district=district, year=year, pollution_level=pollution_level)
        return JsonResponse({'message': 'Data saved successfully.'})
    return JsonResponse({'message': 'Invalid request.'})


def recommend_pollution_level_2024(request):
    historical_data = AirPollutionData.objects.filter(year__gte=2017, year__lte=2023)
    district_avg_pollution = {}
    for data in historical_data:
        if data.district not in district_avg_pollution:
            district_avg_pollution[data.district] = [data.pollution_level]
        else:
            district_avg_pollution[data.district].append(data.pollution_level)

    recommendation_2024 = {}
    for district, pollution_levels in district_avg_pollution.items():
        avg_pollution_level = sum(pollution_levels) / len(pollution_levels)
        recommendation_2024[district] = round(avg_pollution_level)

    return render(request, 'recommendation_template.html', {'recommendation_2024': recommendation_2024})


import os
from django.conf import settings
import matplotlib.pyplot as plt
import os
from django.conf import settings
import matplotlib.pyplot as plt
import json
from django.http import JsonResponse

def display_air_pollution_data(request):
    # Retrieve all unique years from the AirPollutionData objects
    years = AirPollutionData.objects.values_list('year', flat=True).distinct()

    # Create a dictionary to store data for each year
    data_for_years = {}

    # Iterate over each year
    for year in years:
        # Retrieve air pollution data for the current year
        air_pollution_data_year = AirPollutionData.objects.filter(year=year)

        # Extract district names and their corresponding pollution levels
        districts = [data.district for data in air_pollution_data_year]
        pollution_levels = [data.pollution_level for data in air_pollution_data_year]

        # Calculate total pollution levels for each district
        district_pollution_totals = {}
        for district, pollution_level in zip(districts, pollution_levels):
            if district in district_pollution_totals:
                district_pollution_totals[district] += pollution_level
            else:
                district_pollution_totals[district] = pollution_level

        # Store the data for the current year
        data_for_years[year] = district_pollution_totals

    # Serialize data to JSON format
    data_json = json.dumps(data_for_years)

    # Pass the data to the template for rendering
    return render(request, 'air_pollution_data.html', {'data_json': data_json})
def predict_air_quality(user_input):
    # Define thresholds for each category
    thresholds = {
        "Good": {
            "CO": (0, 0.3),
            "NMHC": (0, 0.05),
            "C6H6": (0, 0.03),
            "NO2": (0, 0.02),
            "temp": (0, 25),
            "humidity": (70, 100)
        },
        "Moderate": {
            "CO": (0.3, 0.5),
            "NMHC": (0.05, 0.07),
            "C6H6": (0.03, 0.04),
            "NO2": (0.02, 0.03),
            "temp": (25, 30),
            "humidity": (65, 70)
        },
        "Unhealthy for Sensitive Groups": {
            "CO": (0.5, 1.0),
            "NMHC": (0.07, 0.1),
            "C6H6": (0.04, 0.05),
            "NO2": (0.03, 0.05),
            "temp": (30, 35),
            "humidity": (60, 65)
        },
        "Unhealthy": {
            "CO": (1.0, 2.0),
            "NMHC": (0.1, 0.15),
            "C6H6": (0.05, 0.08),
            "NO2": (0.05, 0.07),
            "temp": (35, 40),
            "humidity": (55, 60)
        },
        "Very Unhealthy": {
            "CO": (2.0, 4.0),
            "NMHC": (0.15, 0.2),
            "C6H6": (0.08, 0.1),
            "NO2": (0.07, 0.1),
            "temp": (40, 45),
            "humidity": (50, 55)
        },
        "Hazardous": {
            "CO": (4.0, float('inf')),
            "NMHC": (0.2, 0.3),
            "C6H6": (0.1, 0.15),
            "NO2": (0.1, 0.15),
            "temp": (45, float('inf')),
            "humidity": (45, 50)
        }
    }

    # Compare input values with thresholds
    for category, params in thresholds.items():
        if all(params[param][0] <= user_input[param] <= params[param][1] for param in params):
            return category

    # If none of the thresholds match, return an error
    return "Error: Unable to determine air quality"


# views.py
import os
import pickle
from django.shortcuts import render
from django.http import JsonResponse
from AirPollution.forms import AirQualityForm  

def classify_air_quality(request):
    if request.method == 'POST':
        form = AirQualityForm(request.POST)
        if form.is_valid():
            # Get form data
            data = form.cleaned_data

            # Load the trained model
            model_path = os.path.join(settings.BASE_DIR, 'myapp', 'models', 'air_quality_model.pkl')
            with open(model_path, 'rb') as file:
                model = pickle.load(file)

            # Prepare input data for classification
            input_data = [data['feature1'], data['feature2'], ...]  # Update with your features

            # Perform classification
            prediction = model.predict([input_data])[0]

            # Convert prediction to human-readable label if needed
            label = 'Good' if prediction == 0 else 'Moderate' if prediction == 1 else 'Unhealthy' if prediction == 2 else 'Hazardous'

            # Return classification result
            return JsonResponse({'prediction': label})

    else:
        form = AirQualityForm()

    return render(request, 'result_1.html', {'form': form})
# ----------------------------------------------------------------
def predict_health_concern(aqi, co, nmhc, c6h6, no2, temp, humidity):
    # Define thresholds for different levels of health concern
    aqi_levels = [(0, 50), (51, 100), (101, 150), (151, 200), (201, 300), (301, 500)]
    health_concerns = ['Good', 'Moderate', 'Unhealthy for Sensitive Groups', 'Unhealthy', 'Very Unhealthy', 'Hazardous']

    # Determine AQI level
    aqi_level = None
    for i, (low, high) in enumerate(aqi_levels):
        if low <= aqi <= high:
            aqi_level = i
            break

    # Determine CO level
    if co <= 4.4:
        co_level = 0
    elif 4.5 <= co <= 9.4:
        co_level = 1
    elif 9.5 <= co <= 12.4:
        co_level = 2
    elif 12.5 <= co <= 15.4:
        co_level = 3
    elif 15.5 <= co <= 30.4:
        co_level = 4
    else:
        co_level = 5

    # Determine NMHC level
    if nmhc <= 0.06:
        nmhc_level = 0
    elif 0.07 <= nmhc <= 0.13:
        nmhc_level = 1
    else:
        nmhc_level = 2

    # Determine C6H6 level
    if c6h6 <= 0.062:
        c6h6_level = 0
    elif 0.063 <= c6h6 <= 0.125:
        c6h6_level = 1
    else:
        c6h6_level = 2

    # Determine NO2 level
    if no2 <= 0.053:
        no2_level = 0
    elif 0.054 <= no2 <= 0.1:
        no2_level = 1
    else:
        no2_level = 2

    # Determine overall health concern level
    max_level = max(aqi_level, co_level, nmhc_level, c6h6_level, no2_level)
    health_concern = health_concerns[max_level]

    return health_concern


# predicted_health_concern = predict_health_concern(aqi, co, nmhc, c6h6, no2, temp, humidity)
# print(f"Predicted health concern for {district}: {predicted_health_concern}")

# ----------------------------------------------------------------
def predict_air_quality(air_quality_instance):
    # Calculate AQI
    aqi = calculate_aqi(air_quality_instance.CO, air_quality_instance.NMHC, air_quality_instance.C6H6, air_quality_instance.NO2)

    # Determine level of health concern and color based on AQI
    if aqi <= 50:
        level_of_concern = "Good"
        color = "green"
    elif aqi <= 100:
        level_of_concern = "Moderate"
        color = "yellow"
    elif aqi <= 150:
        level_of_concern = "Unhealthy for Sensitive Groups"
        color = "orange"
    elif aqi <= 200:
        level_of_concern = "Unhealthy"
        color = "red"
    elif aqi <= 300:
        level_of_concern = "Very Unhealthy"
        color = "purple"
    else:
        level_of_concern = "Hazardous"
        color = "maroon"

    # Add AQI, level of concern, and color to the air_quality_instance
    air_quality_instance.AQI = aqi
    air_quality_instance.level_of_concern = level_of_concern
    air_quality_instance.color = color

    # Save the changes to the database
    air_quality_instance.save()

    return air_quality_instance

def calculate_aqi(co, nmhc, c6h6, no2):
    # Calculate AQI based on formula or method suitable for your application
    # You can use the EPA's AQI calculation formula or any other suitable method
    # For simplicity, let's assume a simple average of the inputs for demonstration purposes
    aqi = (co + nmhc + c6h6 + no2) / 4  # Simple average for demonstration

    return aqi


# views.py
from django.shortcuts import render
from AirPollution.forms import AirQualityForm
from AirPollution.models import AirQuality

def pred(request):
    if request.method == 'POST':
        form = AirQualityForm(request.POST)
        if form.is_valid():
            district = form.cleaned_data['District']
            co = form.cleaned_data['CO']
            nmhc = form.cleaned_data['NMHC']
            c6h6 = form.cleaned_data['C6H6']
            no2 = form.cleaned_data['NO2']
            temp = form.cleaned_data['temp']
            humidity = form.cleaned_data['humidity']

            # Save the form data to the database
            air_quality_instance = AirQuality.objects.create(
                District=district,
                CO=co,
                NMHC=nmhc,
                C6H6=c6h6,
                NO2=no2,
                temp=temp,
                humidity=humidity
            )
            
            air_quality_instance_val = predict_air_quality(air_quality_instance)

            # Render a template with the result
            return render(request, 'result_1.html', {'air_quality_instance': air_quality_instance,'air_quality_instance_val':air_quality_instance_val})
    else:
        form = AirQualityForm()

    return render(request, 'predict_1.html', {'form': form})

