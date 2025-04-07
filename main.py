import pandas as pd
import pprint
import webscraper_module
from model import MistralLLM
# --- Main Logic Function ---
def get_results(company_name, max_budget):
    print(f"Company Name: {company_name}, Max Budget: {max_budget}")

    # Read energy consumption CSV
    df = pd.read_csv('energy_consumption.csv')

    print(f"Dataframe:\n{df}")

    #Scrape Amazon(Sariya) - Done
    devices_df = df.sort_values(by='Energy Consumed (kWh)', ascending=False)
    amazon_results_df = webscraper_module.search_amazon_from_df(devices_df)
    amazon_results_df.to_csv('amazon_results.csv', index=False)

    #Find the best match Among the listed devices to buy(Sreehari)
    """ 
    Use the Amazon Results Data Frame to find the best match
    """
    df1=pd.read_csv('example_amazon_result.csv')
    amazon_df=df1.sort_values(by='value',ascending=False)
    energy_text = devices_df.to_string(index=False)
    amazon_text = amazon_df.to_string(index=False)

    prompt=" "
    llm=MistralLLM()
    response=llm.invoke(prompt)
    

    #Generate the Projections(Cherishma & Madhu)
    """
    Use initial consumption data to generate initial projection
    Then Use Sreehari's results to generate the data for the next months. 
    """

    #Generate Summary(Glen)
    """
      Relatively small job, feeding into LLM.
    """

     #Example of how the RESPONSE should look like, follow the same SCHEMA
    #"message" : Returns a Message summary generated by the LLM
    #"chartData" : Returns a List of new Items that are suggested to purchase.
    #   "name" - Name of the Item
    #   "value" - Value of the Item
    #   "url" - URL of the Item
    #"budgetComparisonData" : Returns values for each month
    #   "month" - Name of the Month
    #   "initial" - Takes the consumption data raw and showcases what it will be for the month
    #   "improved" - Modifies "initial" and showcases what it will be for the month with the replaced items
    #
    # Sample Output is given below 
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
