import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

#Load dataset
df = pd.read_csv('crop_data.csv')

#Convert text data (soil type) to numbers
df['soil_type'] = df['soil_type'].astype('category').cat.codes

#Split data info inputs (x) and output (y)
x = df.drop(columns=['top'])
y = df['crop']

#Train ML model
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, r)