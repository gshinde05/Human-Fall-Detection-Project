
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("motion.csv")
X = df.drop('Motion', axis=1)
y = df['Motion']

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, '../backend/model.pkl')
