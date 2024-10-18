ISO601 Order Processing Tutorial
Welcome to the ISO601 Order Processing Project! This project is a midterm project turned guide that will walk you through how to set up, run, and customize the order processing Python script found in this repository. Whether you're a beginner or an experienced user, this tutorial will help you understand the code and get everything working smoothly.

Table of Contents
Overview
Prerequisites
Setup
How the Script Works
Running the Script
Input JSON Structure
Output JSON Files
Customization and Extension
Troubleshooting
License

1. Overview
This project provides a Python script that processes customer orders stored in a JSON file. It:

- Extracts customer names and formats phone numbers.
- Tracks how often each item is ordered and the item’s price.
- Saves customer and item data into separate JSON files for easy reference.
- The script makes it easy to process orders, ideal for quick analytics or integrations with other applications.

2. Prerequisites
Before using this project, make sure you have the following:

Python 3.x installed. You can download it from Python's official website.
A JSON file with orders in the correct format (see example below).
Optional but helpful:

Basic knowledge of how to run Python scripts.
Familiarity with GitHub and command-line tools.

3. Setup
Clone the repository to your local machine:

git clone https://github.com/ahmedshifathedataengineer/iso601.git
cd iso601

Install Python (if not already installed):
Follow this guide to install Python on your system.

Verify your Python installation by running:

python --version

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

Install any required packages:
This project doesn’t use external dependencies, so no additional packages are needed.

4. How the Script Works
The midterm.py script reads a JSON file (example_orders.json) containing customer orders. It:

- Extracts customer names and formats phone numbers.
- Processes each item to track prices and the number of orders.
- Saves the processed data into:
- customers.json: Contains phone numbers and customer names.
- items.json: Contains item names, prices, and the number of times each item was ordered.

5. Running the Script
Place your JSON file (e.g., example_orders.json) in the same directory as the script.

Run the Python script:

python midterm.py 

Verify the output:

- Check customers.json for customer data.
Check items.json for item data.

6. Input JSON Structure
The script expects the input JSON file to have the following structure:

json
Copy code
[
    {
        "name": "John Doe",
        "phone": "+1-123-456-7890",
        "items": [
            
                "name": "Widget A",
                "price": 9.99
            },
            {
                "name": "Widget B",
                "price": 14.99
            }
        ]
    }
]

Explanation:
- name: Customer's full name.
- phone: Customer's phone number, which will be formatted by the script.
- items: A list of items with their names and prices.
#This is the core of the project.

7. Output JSON Files
After running the script, two JSON files will be created:

customers.json
Example:

json
Copy code
{
    "(123) 456-7890": "John Doe"
}
items.json
Example:

json
Copy code
{
    "Widget A": {
        "price": 9.99,
        "orders": 1
    },
    "Widget B": {
        "price": 14.99,
        "orders": 1
    }
}

8. Customization and Extension
You can modify the script to fit your needs. Here are a few ideas:

Support additional fields: Add more details to each order, such as shipping addresses or discounts.
Log errors to a file: Implement logging to record any missing fields or formatting errors.
Add unit tests: Ensure the script works as expected by writing automated tests.
To modify the phone formatting function, edit the format_phone_number() function in midterm.py.

9. Troubleshooting
Problem: The script throws a JSONDecodeError.
Solution: Ensure the input JSON file is properly formatted. Use JSONLint to validate the structure.

Problem: Output files (customers.json or items.json) are not created.
Solution: Make sure you have write permissions for the directory.

Problem: No data appears in the output files.
Solution: Ensure the input JSON file contains valid orders with the expected keys (name, phone, items).

10. License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributing
Feel free to submit pull requests or open issues if you have suggestions or find bugs. Contributions are welcome!


