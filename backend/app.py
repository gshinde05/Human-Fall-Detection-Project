
from flask import Flask, request, render_template
import joblib
import firebase_admin
from firebase_admin import credentials, db
from firebase_config import init_firebase

app = Flask(__name__)
model = joblib.load('model.pkl')
init_firebase()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def predict_motion():
    data = [float(request.form[k]) for k in ['ax', 'ay', 'az', 'gx', 'gy', 'gz']]
    prediction = model.predict([data])[0]
    db.reference('fall_data').push({'data': data, 'prediction': prediction})
    return str(prediction)

if __name__ == '__main__':
    app.run(debug=True)
