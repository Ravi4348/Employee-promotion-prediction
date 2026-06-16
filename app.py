from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained model from pickle file
with open('Assets/pickle/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

# Route for the main page (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Route for predicting employee promotion
@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    age = float(request.form['age'])
    experience = float(request.form['experience'])
    job_title = int(request.form['job_title'])  # Job Title is passed as a number (1, 2, 3, etc.)

    # Convert input data into numpy array for prediction
    employee_data = np.array([age, experience, job_title]).reshape(1, -1)

    # Make the prediction
    prediction = model.predict(employee_data)

    # Interpret the prediction
    result = "Promoted" if prediction[0] == 1 else "Not Promoted"
    return render_template('index.html', prediction_result=result)

if __name__ == "__main__":
    app.run(debug=True)
