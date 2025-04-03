# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request 
from flask_cors import CORS
from main import get_results
import pandas as pd

# creating a Flask app 
app = Flask(__name__) 
CORS(app)

# on the terminal type: curl http://127.0.0.1:5000/api/eco_react 
# returns "API Works" when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/api/eco_react', methods = ['GET', 'POST']) 
def input_form(): 
    if(request.method == 'GET'): 
        data = "API Works"
        return jsonify({'data': data})

    if(request.method == 'POST'):
        #Print Company Details
        company_name = request.form['companyName']
        max_budget = float(request.form['maxBudget'])

        #Print Consumption Data
        file = request.files['file']
        file.save('energy_consumption.csv')

        results_data = get_results(company_name,max_budget)

        return jsonify(results_data), 200
  
# driver function 
if __name__ == '__main__': 
    app.run(debug = True) 
