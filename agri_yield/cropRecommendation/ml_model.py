import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os


# Get the absolute path to the CSV file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "data", "crop_data.csv")

#Load dataset
df = pd.read_csv('crop_data.csv')

#Convert text data (soil type) to numbers
df['soil_type'] = df['soil_type'].astype('category').cat.codes

#Split data info inputs (x) and output (y)
x = df.drop(columns=['top'])
y = df['crop']

#Train ML model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

#Save Model
with open('crop_recommendation.pkl', 'wb') as file:
    pickle.dump(model, file)
