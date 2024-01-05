import json
import subprocess
import datetime

def get_current_date_string():
  """
  Returns the current date as a string in the format 'YYYY-MM-DD'.

  Returns:
    str: The current date as a string.
  """
  now = datetime.datetime.now()
  return now.strftime("%Y-%m-%d")

def download_lineage_data():
  """
  Downloads the lineage data from the specified URL.
  """
  subprocess.call(['wget', 'https://github.com/cov-lineages/lineages-website/raw/master/_data/lineage_data.full.json'])

def remove_lineage_data():
  """
  Removes the lineage_data.full.json file.
  """
  subprocess.call(['rm', 'lineage_data.full.json'])

def process_lineage_data(lineage_data):
  output_file = f"pangolist_{get_current_date_string()}.txt"
  output_file2 = f"voclist_{get_current_date_string()}.txt"

  lineage_mapping = {
    "B.1.1.529.": "Omicron",
    "B.1.617.2.": "Delta",
    "B.1.1.7.": "Alpha",
    "B.1.177.": "20E"
  }

  with open(output_file, 'w') as out_file, open(output_file2, 'w') as out_file2:
    for key, value in lineage_data.items():
      lineage = key.split(':')[0]
      description = value.get('Description', 'No description available')
      out_file.write(f"{lineage}: {description}\n")
      if lineage in lineage_mapping:
        out_file2.write(f"{lineage}: {lineage_mapping[lineage]}\n")

def main():
  download_lineage_data()

  with open('lineage_data.full.json', 'r') as f:
    data = json.load(f)

  process_lineage_data(data)

  remove_lineage_data()

if __name__ == "__main__":
  main()