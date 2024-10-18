# Order Processing Script

This project provides a Python script to process customer orders stored in a JSON file. It extracts customer information and item details, formats phone numbers, and saves the extracted data into separate JSON files.

## Features

- Reads orders from a JSON file.
- Extracts and formats customer names and phone numbers.
- Tracks the number of orders and total price for each item.
- Saves customer and item data into `customers.json` and `items.json`.

## How to Use

1. **Prepare the JSON File:** Ensure your orders are structured correctly. Each order should have a `name`, `phone`, and an `items` list with `name` and `price` fields. Example:

    ```json
    [
      {
        "name": "John Doe",
        "phone": "+1-123-456-7890",
        "items": [
          {
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
    ```

2. **Run the Script:**
   Place your JSON file (e.g., `example_orders.json`) in the same directory as the script. Run the script using:

   ```bash
   python orders_processor.py
