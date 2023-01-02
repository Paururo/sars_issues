import json
import subprocess
import datetime
# paururo
# Get the current date and time
now = datetime.datetime.now()
# Format the date and time as a string
date_string = now.strftime("%Y-%m-%d")
output_file = f"pangolist_{date_string}.txt"
# Download the JSON file from GitHub
# Run the wget command using subprocess.call()
subprocess.call(['wget', 'https://raw.githubusercontent.com/cov-lineages/lineages-website/master/_data/lineage_data.full.json'])
# Open the JSON file
with open('lineage_data.full.json', 'r') as f:
  data = json.load(f)
# Open a new file in write mode
with open(output_file, 'w') as out_file:
  # Loop through the keys in the data dictionary
  for key in data:
    try:
      # Write the key and description to the output file
      out_file.write(f"{key}: {data[key]['Description']}\n")
    except (TypeError, KeyError):
      out_file.write(f"{key}: No description available\n")