#parselog.py
#parses suricata eve.json for alerts and provides in human readable format.

import json
import sys

# Check if a file path is provided
if len(sys.argv) < 2:
    print("Usage: python3 parselog.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

signatures = {}
categories = {}

# File processing
try:
    with open(file_path, 'r') as f:
        for line in f:
            try:
                event = json.loads(line)
                # Only process events with an alert section
                if 'alert' in event:
                    if 'signature' in event['alert']:
                        signature = event['alert']['signature']
                        signatures[signature] = signatures.get(signature, 0) + 1
                    if 'category' in event['alert']:
                        category = event['alert']['category']
                        categories[category] = categories.get(category, 0) + 1
            except json.JSONDecodeError:
                # Skip any lines that aren't valid JSON
                continue
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
    sys.exit(1)


# Sort the results by count in descending order
sorted_signatures = sorted(signatures.items(), key=lambda item: item[1], reverse=True)
sorted_categories = sorted(categories.items(), key=lambda item: item[1], reverse=True)

# Print the results
print('Unique signatures and their counts:')
for signature, count in sorted_signatures:
    print(f'  {signature}: {count}')

print('\nUnique categories and their counts:')
for category, count in sorted_categories:
    print(f'  {category}: {count}')
