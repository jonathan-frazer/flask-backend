# Energy Efficiency Optimization System

A Flask-based backend system that analyzes energy consumption data and provides recommendations for energy-efficient device purchases within a specified budget.

## Project Overview

This system helps companies optimize their energy consumption by:

1. Analyzing current energy usage patterns
2. Scraping Amazon for energy-efficient alternatives
3. Using AI to recommend optimal device replacements
4. Generating projections of energy savings
5. Providing a detailed analysis of cost-benefit scenarios

## Key Components

- main.py: Core logic for energy analysis and recommendations
- module_webscraper.py: Handles Amazon product scraping
- module_langchain.py: Implements AI-powered analysis using Mistral LLM
- model.py: Data models and structures
- app.py: Flask application entry point (DO NOT MODIFY)

## Data Files

- energy_consumption.csv: Input data for energy consumption analysis
- amazon_results.csv: Scraped product data from Amazon
- example_amazon_results.csv: Sample data for testing

## _Contributor Guidelines_

### Code Structure and Modification Rules

- _DO NOT MODIFY_ app.py - This is the core Flask application file and should remain unchanged
- All new features and modifications should be implemented in main.py
- Follow the established input/output format strictly
- Maintain backward compatibility with existing code

### Development Workflow

1. _Before Starting Development_

   - Create a new branch for your feature/fix
   - Ensure your virtual environment is activated
   - Install all dependencies using pip install -r requirements.txt

2. _During Development_

   - Add clear comments for complex logic
   - Test your changes locally before committing

3. _Package Management_

   - If you need to add new packages:
     - Install using pip install <package-name>
     - Update requirements.txt using pip freeze > requirements.txt
   - Document any new dependencies in your pull request

4. _Testing Requirements_

   - Test your changes with various input scenarios
   - Verify that main.py returns the correct output format
   - Ensure no changes are made to app.py
   - Test with both sample and real data

5. _Pull Request Guidelines_

   - Provide a clear description of changes

## _Development Environment_

### Use a virtual environment

- Install virtualenv using pip install virtualenv.
- Create a virtual environment using virtualenv venv.
- Activate the virtual environment using venv\Scripts\activate.

### Install packages

- Run pip install -r requirements.txt to install the required packages.

## Dependencies

The project uses several key Python packages:

- Flask: Web framework
- Pandas: Data analysis
- BeautifulSoup4: Web scraping
- LangChain: AI integration
- Requests: HTTP requests
- Flask-CORS: Cross-origin resource sharing

See requirements.txt for the complete list of dependencies.
