import pandas as pd
import pprint

def get_results(company_name, max_budget):

    #INPUTS(I've printed them out for your convenience):-

    # Company Name : str
    # Max Budget : float
    print(f"Company Name: {company_name}, Max Budget: {max_budget}")

    # CSV File - (Read it to see it's format)
    df = pd.read_csv('energy_consumption.csv')
    print(f"Dataframe:-\n{df}")



    #OUTPUTS:-

    #Example of how the RESPONSE should look like, follow the same SCHEMA
    #"message" : Returns a Simple message summary
    #"chartData" : Returns a List of new Items that are suggested to purchase.
    #   "name" - Name of the Item
    #   "value" - Value of the Item
    #   "url" - URL of the Item
    #"budgetComparisonData" : Returns values for each month
    #   "month" - Name of the Month
    #   "initial" - Takes the consumption data raw and showcases what it will be for the month
    #   "improved" - Modifies "initial" and showcases what it will be for the month with the replaced items

    return {
            "message": f"We've analyzed {company_name}'s data with a budget of ₹{max_budget}. Based on your CSV data, we recommend focusing on renewable energy investments and waste reduction programs to maximize eco-impact within your budget constraints.",
            "chartData": [
                {"name": "Air Conditioning", "value": max_budget * 0.4, "url": "https://www.example.com"},
                {"name": "Refrigerator", "value": max_budget * 0.35, "url": "https://www.example.com"},
                {"name": "Server Room", "value": max_budget * 0.25, "url": "https://www.example.com"},
                {"name": "Recycling", "value": max_budget * 0.15, "url": "https://www.example.com"},
                {"name": "Waste Segregation", "value": max_budget * 0.1, "url": "https://www.example.com"}
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

#Gives example of output if run directly
if __name__ == '__main__': 
    print("\n\nInput:-")
    result_data = get_results("Chandan Enterprises", 12000)
    print("\n\nOutput:-")
    pprint.pprint(result_data)