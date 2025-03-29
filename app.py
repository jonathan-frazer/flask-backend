# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request 
from flask_cors import CORS  
import json
import pandas as pd

# creating a Flask app 
app = Flask(__name__) 
CORS(app)

def get_results(company_name, max_budget,file_data):
    print(f"Company Name: {company_name}, Max Budget: {max_budget}")
    df = pd.read_csv(file_data)
    df.head(10)

    return {
            "message": f"We've analyzed {request.form['companyName']}'s data with a budget of ₹{max_budget}. Based on your CSV data, we recommend focusing on renewable energy investments and waste reduction programs to maximize eco-impact within your budget constraints.",
            "chartData": [
                {"name": "Solar ENERGY", "value": max_budget * 0.4, "url": "https://www.google.co.in"},
                {"name": "Wind ENERGY", "value": max_budget * 0.35, "url": "https://www.google.co.in"},
                {"name": "Hydro ENERGY", "value": max_budget * 0.25, "url": "https://www.google.co.in"},
                {"name": "Recycling", "value": max_budget * 0.15, "url": "https://www.google.co.in"},
                {"name": "Composting", "value": max_budget * 0.1, "url": "https://www.google.co.in"},
                {"name": "Waste Reduction", "value": max_budget * 0.05, "url": "https://www.google.co.in"},
                {"name": "Water Conservation", "value": max_budget * 0.2, "url": "https://www.google.co.in"},
                {"name": "Rainwater Harvesting", "value": max_budget * 0.15, "url": "https://www.google.co.in"},
                {"name": "Greywater Recycling", "value": max_budget * 0.1, "url": "https://www.google.co.in"},
                {"name": "Carbon Offsetting", "value": max_budget * 0.1, "url": "https://www.google.co.in"},
                {"name": "Carbon Capture", "value": max_budget * 0.05, "url": "https://www.google.co.in"},
                {"name": "Sustainable Forestry", "value": max_budget * 0.05, "url": "https://www.google.co.in"},
            ],
            "budgetComparisonData": [
                {"month": "Jan", "initial": max_budget * 0.12, "improved": max_budget * 0.1},
                {"month": "Feb", "initial": max_budget * 0.14, "improved": max_budget * 0.11},
                {"month": "Mar", "initial": max_budget * 0.13, "improved": max_budget * 0.09},
                {"month": "Apr", "initial": max_budget * 0.15, "improved": max_budget * 0.1},
                {"month": "May", "initial": max_budget * 0.16, "improved": max_budget * 0.11},
                {"month": "Jun", "initial": max_budget * 0.17, "improved": max_budget * 0.12},
                {"month": "Jul", "initial": max_budget * 0.18, "improved": max_budget * 0.13},
                {"month": "Aug", "initial": max_budget * 0.19, "improved": max_budget * 0.14},
            ],
        }

# on the terminal type: curl http://127.0.0.1:5000/api/eco_react 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/api/eco_react', methods = ['GET', 'POST']) 
def input_form(): 
    if(request.method == 'GET'): 
        data = "hello world"
        return jsonify({'data': data})

    if(request.method == 'POST'):
        #Print Company Details
        company_name = request.form['companyName']
        max_budget = float(request.form['maxBudget'])

        #Print Consumption Data
        file_data = request.files['file'].read().decode('utf-8')

        #Results(Follow this format style for it to work)
        results_data = get_results(company_name,max_budget,file_data)

        return jsonify(results_data), 200
  
# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 