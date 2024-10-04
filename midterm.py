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
    # Open the input JSON file and read the data
    with open(file_name, 'r') as file:
        orders = json.load(file)

    # Initialize dictionaries for customers and items
    customers = {}
    items = defaultdict(lambda: {'price': 0.0, 'orders': 0})

    # Loop through each order and extract relevant information
    for order in orders:
        # Extract and format customer details
        customer_name = order.get("customer_name")
        phone_number = format_phone_number(order.get("customer_phone"))

        if customer_name and phone_number:
            customers[phone_number] = customer_name

        # Extract item details
        for item in order.get("order_items", []):
            item_name = item.get("item_name")
            item_price = item.get("item_price", 0.0)
            
            if item_name:
                # Update item details
                items[item_name]['price'] = item_price
                items[item_name]['orders'] += 1

    # Save the customers and items data to separate JSON files
    with open('customers.json', 'w') as customer_file:
        json.dump(customers, customer_file, indent=4)
    with open('items.json', 'w') as items_file:
        json.dump(items, items_file, indent=4)
    print("Data successfully saved.")

# Example usage
process_orders('example_orders.json')
