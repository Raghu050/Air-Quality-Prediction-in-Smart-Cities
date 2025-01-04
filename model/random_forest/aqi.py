import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

def classify_air_quality(data_path, model_save_path):
    # Load data
    data = pd.read_csv(data_path)

    # Preprocess data
    # Assuming 'Date', 'Time', and other features are columns in the CSV

    # Convert 'Date' and 'Time' columns to datetime
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
    data['Time'] = pd.to_datetime(data['Time'], format='%H.%M.%S').dt.time

    # Drop irrelevant columns like 'Date', 'Time', etc.
    data = data.drop(columns=['Date', 'Time'])

    # Handle missing values (if any)
    data = data.dropna()

    # Classify air quality based on CO(GT) levels
    data['Air_Quality'] = pd.cut(data['CO(GT)'],
                                 bins=[-1, 2, 4, 6, float('inf')],
                                 labels=['Good', 'Moderate', 'Unhealthy', 'Hazardous'])

    # Encode target variable
    le = LabelEncoder()
    data['Air_Quality'] = le.fit_transform(data['Air_Quality'])

    # Split data into features and target variable
    X = data.drop(columns=['CO(GT)', 'Air_Quality'])  # Use other columns as features
    y = data['Air_Quality']  # Air quality as target variable

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train a random forest classifier
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model as a pickle file
    with open(model_save_path, 'wb') as file:
        pickle.dump(model, file)

    print("Model saved successfully as", model_save_path)

    return model

def visualize_predictions(model, X_test, y_test):
    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    # Plot confusion matrix
    plt.figure(figsize=(8, 6))
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=['Good', 'Moderate', 'Unhealthy', 'Hazardous'],
                yticklabels=['Good', 'Moderate', 'Unhealthy', 'Hazardous'])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.show()

    # Plot feature importances
    if hasattr(model, 'feature_importances_'):
        feature_importances = model.feature_importances_
        plt.figure(figsize=(10, 6))
        sns.barplot(x=feature_importances, y=X_test.columns)
        plt.xlabel('Feature Importance')
        plt.ylabel('Features')
        plt.title('Feature Importances')
        plt.show()

# Example usage
data_path = "your_data.csv"
model_save_path = "air_quality_model.pkl"

# Train the model
trained_model = classify_air_quality(data_path, model_save_path)

# Load test data
data = pd.read_csv(data_path)
X_test = data.drop(columns=['CO(GT)', 'Air_Quality']).iloc[-100:]  # Example: Using last 100 samples as test data
y_test = data['Air_Quality'].iloc[-100:]  # Example: Using last 100 samples as test labels

# Visualize predictions
visualize_predictions(trained_model, X_test, y_test)
