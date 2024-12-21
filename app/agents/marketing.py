import csv
import os
from pydantic_ai import Agent
from app.dependencies.dependencies import SupportDependencies

marketing_agent = Agent(
    'openai:gpt-4o-mini',
    deps_type=SupportDependencies,
    system_prompt=(
        'You are a marketing agent in our bank'
        'For now you only save the customer name in our marking system using tool `save_customer_name`'
    ),
)

@marketing_agent.tool_plain
async def save_customer_name(customer_name: str, customer_id: int) -> None:
    """Saves the customer's name and tracks how many times their info is captured."""
    csv_file_path = 'customer_name.csv'

    # If the file does not exist, create it and write the header
    if not os.path.exists(csv_file_path):
        with open(csv_file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['customer_id', 'customer_name', 'inquiries_count'])

    # Read the existing data to check if the customer already exists
    customer_found = False
    rows = []
    with open(csv_file_path, 'r', newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Check if the customer ID already exists and update the inquiry count
    for row in rows:
        if row[0] == str(customer_id):
            row[2] = str(int(row[2]) + 1)  # Increment the inquiry count
            customer_found = True
            break

    # If the customer was not found, add a new row with inquiry count starting from 0
    if not customer_found:
        rows.append([str(customer_id), customer_name, '0'])

    # Write the updated data back to the CSV file
    with open(csv_file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)