import pandas as pd
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pickle

# Load the dataset (ensure you replace this with the correct path to your dataset)
data = pd.read_csv("TEST\Employee 1000x.csv")  # Ensure the correct file path is provided

# Check the first few rows of the dataset to understand its structure
print(data.head())

# Ensure that 'Date of Birth' is in datetime format
data['Date of birth'] = pd.to_datetime(data['Date of birth'], format='%d-%m-%y')

# Calculate Age (current year - birth year)
current_year = datetime.now().year
data['Age'] = current_year - data['Date of birth'].dt.year

# Example Experience calculation (assuming it equals Age for now)
data['Experience'] = data['Age']  # You can modify this logic if actual experience data is available

# Add a random Promotion Status (0 or 1) based on the length of the dataset
# Create a list with random 0s and 1s to represent promotion status
np.random.seed(42)  # Set seed for reproducibility
data['Promotion Status'] = np.random.choice([0, 1], size=len(data), p=[0.5, 0.5])  # 50% chance for promotion

# Ensure the dataset has the correct number of rows (10000)
print(data.shape)  # Should print (10000, X) where X is the number of columns

# Prepare features (X) and target variable (y)
X = data[['Age', 'Experience', 'Job Title']]  # Features: Age, Experience, Job Title
y = data['Promotion Status']  # Target: Promotion Status (1 or 0)

# Convert Job Title to numerical values using a mapping
job_title_mapping = {
    "Editor, commissioning": 1,
    "Broadcast engineer": 2,
    "Industrial buyer": 3,
    "Multimedia specialist": 4,
    # Add more mappings as needed for other job titles
}

# Map job titles to numeric values
X['Job Title'] = X['Job Title'].map(job_title_mapping)

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)  # Increase n_estimators if necessary
model.fit(X_train, y_train)

# Save the trained model as a pickle file
with open('Assets/pickle/model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved successfully!")
