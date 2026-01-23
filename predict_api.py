import sys
import json
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open('rf_classifier.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

def predict(data):
    """Prediction function"""
    male = data.get('male')
    age = float(data.get('age'))
    currentSmoker = data.get('currentSmoker')
    cigsPerDay = float(data.get('cigsPerDay'))
    BPMeds = data.get('BPMeds')
    prevalentStroke = data.get('prevalentStroke')
    prevalentHyp = data.get('prevalentHyp')
    diabetes = data.get('diabetes')
    totChol = float(data.get('totChol'))
    sysBP = float(data.get('sysBP'))
    diaBP = float(data.get('diaBP'))
    BMI = float(data.get('BMI'))
    heartRate = float(data.get('heartRate'))
    glucose = float(data.get('glucose'))
    
    # Encode categorical variables
    male_encoded = 1 if male.lower() == "male" else 0
    currentSmoker_encoded = 1 if currentSmoker.lower() == "yes" else 0
    BPMeds_encoded = 1 if BPMeds.lower() == "yes" else 0
    prevalentStroke_encoded = 1 if prevalentStroke.lower() == "yes" else 0
    prevalentHyp_encoded = 1 if prevalentHyp.lower() == "yes" else 0
    diabetes_encoded = 1 if diabetes.lower() == "yes" else 0

    # Prepare features array
    features = np.array([[male_encoded, age, currentSmoker_encoded, cigsPerDay, BPMeds_encoded, prevalentStroke_encoded,
                          prevalentHyp_encoded, diabetes_encoded, totChol, sysBP, diaBP, BMI, heartRate, glucose]])

    # Scale the features
    scaled_features = scaler.transform(features)

    # Predict using the model
    result = model.predict(scaled_features)
    probability = model.predict_proba(scaled_features)

    return {
        'prediction': int(result[0]),
        'probability': float(probability[0][1]),
        'result': 'High Risk' if result[0] == 1 else 'Low Risk'
    }

if __name__ == '__main__':
    if len(sys.argv) > 1:
        data = json.loads(sys.argv[1])
        result = predict(data)
        print(json.dumps(result))
