#Goals

#Python script that reads JSON orders from a file

import json
import re
from collections import defaultdict

# Function to format phone numbers
def format_phone_number(phone):
    if phone:
        phone = re.sub(r'\D', '', phone)  # Remove non-digit characters
        if len(phone) == 10:
            return f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    return phone

def process_orders(file_name):
    try:
        # Open the input JSON file and read the data
        with open(file_name, 'r') as file:
            orders = json.load(file)
        print("Orders loaded successfully.")
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        return

    # Initialize dictionaries for customers and items
    customers = {}
    items = defaultdict(lambda: {'price': 0.0, 'orders': 0})

    # Loop through each order and extract relevant information
    for order in orders:
        # Extract and format customer details (adjusted for the keys in your JSON file)
        customer_name = order.get("name")
        phone_number = format_phone_number(order.get("phone"))

        if customer_name and phone_number:
            customers[phone_number] = customer_name

        # Debugging: Log each order being processed
        print(f"Processing order for {customer_name} with phone {phone_number}")

        # Extract item details (adjusted for the keys in your JSON file)
        for item in order.get("items", []):
            item_name = item.get("name")
            item_price = item.get("price", 0.0)

            if item_name:
                # Update item details
                items[item_name]['price'] = item_price
                items[item_name]['orders'] += 1
                # Debugging: Log each item being processed
                print(f"Item processed: {item_name}, Price: {item_price}")
            else:
                print(f"Missing item details in order: {order}")

    # Save the customers and items data to separate JSON files
    try:
        with open('customers.json', 'w') as customer_file:
            json.dump(customers, customer_file, indent=4)
        with open('items.json', 'w') as items_file:
            json.dump(items, items_file, indent=4)
        print("Data successfully saved.")
    except IOError as e:
        print(f"Error writing to JSON files: {e}")

# Example usage
process_orders('example_orders.json')

