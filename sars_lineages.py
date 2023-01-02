import json
import subprocess
import datetime
# Get the current date and time
now = datetime.datetime.now()
# Format the date and time as a string
date_string = now.strftime("%Y-%m-%d")
output_file = f"pangolist_{date_string}.txt"
# Download the JSON file from GitHub
# Run the wget command using subprocess.call()
subprocess.call(['wget', 'https://github.com/cov-lineages/lineages-website/raw/master/_data/lineage_data.full.json'])
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

output_file2 = f"voclist_{date_string}.txt"
with open(output_file2, 'w') as outfile2:
  with open(output_file, 'r') as in_file:
    for line in in_file:
      l = line.strip('\n').split(':')[0]
      if "*" not in line:
        if "B.1.1.529." in line:
          outfile2.write(f"{l}:Omicron\n")
        elif "B.1.617.2." in line:
          outfile2.write(f"{l}:Delta\n")
        elif "B.1.1.7." in line:
          outfile2.write(f"{l}:Alpha\n")
        elif "B.1.177." in line:
          outfile2.write(f"{l}:20E\n")

  outfile2.write("B.1.177:20E\n")
  outfile2.write("B.1.1.7:Alpha\n")
  outfile2.write("B.1.617.2:Omicron\n")
  outfile2.write("B.1.1.529:Delta\n")

subprocess.call(['rm', 'lineage_data.full.json'])