from lib2to3.pgen2.tokenize import double3prog

from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
app = Flask(__name__)

model = pickle.load(open('LinearRegression.pkl', 'rb'))
car = pd.read_csv('train.csv')

@app.route('/')
def index():
    # Weight_kgpi
    # Horsepower
    Cylinders = sorted(car['Cylinders'].unique())
    Fuel_Type = sorted(car['Fuel_Type'].unique())
    Road_Type = sorted(car['Road_Type'].unique())
    Age_years = sorted(car['Age_years'].unique())
    return render_template('index.html',Cylinders=Cylinders, Fuel_Type=Fuel_Type,Road_Type=Road_Type,Age_years=Age_years)

@app.route('/predict', methods=['POST'])
def predict():
    Cylinders = int(request.form.get('Cylinders'))
    Fuel_Type = request.form.get('Fuel_Type')
    Road_Type = request.form.get('Road_Type')
    Age_years = float(request.form.get('Age_years'))
    Weight_kg = float(request.form.get('Weight_kg'))
    Horsepower = float(request.form.get('Horsepower'))
    # print(car['Cylinders'].unique())

    print(Cylinders, Fuel_Type, Road_Type, Age_years, Weight_kg, Horsepower)
    prediction = model.predict(pd.DataFrame(columns = ['Weight_kg','Horsepower','Cylinders','Fuel_Type','Road_Type','Age_years'], data=[[Weight_kg,Horsepower,Cylinders,Fuel_Type,Road_Type,Age_years]]))
    # print(prediction)
    return str(np.round(prediction[0],2))
if __name__ == '__main__':
    app.run()
