#Python script that reads JSON orders from a file

import json  # For reading and writing JSON data
import re  # For handling regular expressions
from collections import defaultdict  # To initialize dictionaries with default values

# Function to format phone numbers into a standard (XXX) XXX-XXXX format
def format_phone_number(phone):
    if phone:
        # Remove any non-digit characters from the phone number
        phone = re.sub(r'\D', '', phone)
        # Ensure the phone number is exactly 10 digits before formatting
        if len(phone) == 10:
            return f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    # Return the original phone number if it doesn't meet the formatting criteria
    return phone

# Function to process orders from a JSON file
def process_orders(file_name):
    try:
        # Attempt to open and read the contents of the specified JSON file
        with open(file_name, 'r') as file:
            orders = json.load(file)  # Load the JSON data into a Python dictionary
        print("Orders loaded successfully.")
    except json.JSONDecodeError as e:
        # Handle JSON decoding errors if the file is not correctly formatted
        print(f"Error reading JSON file: {e}")
        return

    # Initialize dictionaries to store customer information and item details
    customers = {}  # Stores phone numbers as keys and customer names as values
    items = defaultdict(lambda: {'price': 0.0, 'orders': 0})  # Tracks item data

    # Loop through each order to extract relevant details
    for order in orders:
        # Extract customer details from the order (keys should match your JSON schema)
        customer_name = order.get("name")  # Get the customer's name
        phone_number = format_phone_number(order.get("phone"))  # Format the phone number

        if customer_name and phone_number:
            # Store the customer's name with the formatted phone number as the key
            customers[phone_number] = customer_name

        # Debugging: Print each order being processed
        print(f"Processing order for {customer_name} with phone {phone_number}")

        # Extract and process the items within the order
        for item in order.get("items", []):
            item_name = item.get("name")  # Get the item's name
            item_price = item.get("price", 0.0)  # Get the item's price (default to 0.0)

            if item_name:
                # Update the item details: total price and order count
                items[item_name]['price'] = item_price
                items[item_name]['orders'] += 1

                # Debugging: Print each item being processed
                print(f"Item processed: {item_name}, Price: {item_price}")
            else:
                # Print a warning if item details are missing in the order
                print(f"Missing item details in order: {order}")

    # Save the extracted customer and item data to JSON files
    try:
        with open('customers.json', 'w') as customer_file:
            json.dump(customers, customer_file, indent=4)  # Save customer data
        with open('items.json', 'w') as items_file:
            json.dump(items, items_file, indent=4)  # Save item data
        print("Data successfully saved.")
    except IOError as e:
        # Handle file writing errors
        print(f"Error writing to JSON files: {e}")

# Example usage of the script with a sample input file
process_orders('example_orders.json')


# Example usage
process_orders('example_orders.json')

