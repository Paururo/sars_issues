import json
import subprocess
import datetime

# Get the current date and time
now = datetime.datetime.now()
# Format the date and time as a string
date_string = now.strftime("%Y-%m-%d")
output_file = f"pangolist_{date_string}.txt"
output_file2 = f"voclist_{date_string}.txt"

# Download the JSON file from GitHub
subprocess.call(['wget', 'https://github.com/cov-lineages/lineages-website/raw/master/_data/lineage_data.full.json'])

# Open the JSON file
with open('lineage_data.full.json', 'r') as f:
  data = json.load(f)

# Define lineage mapping
lineage_mapping = {
  "B.1.1.529.": "Omicron",
  "B.1.617.2.": "Delta",
  "B.1.1.7.": "Alpha",
  "B.1.177.": "20E"
}

# Process data and write to output files
with open(output_file, 'w') as out_file, open(output_file2, 'w') as out_file2:
  for key, value in data.items():
    lineage = key.split(':')[0]
    description = value.get('Description', 'No description available')
    out_file.write(f"{lineage}: {description}\n")
    if lineage in lineage_mapping:
      out_file2.write(f"{lineage}: {lineage_mapping[lineage]}\n")

# Remove the downloaded JSON file
subprocess.call(['rm', 'lineage_data.full.json'])