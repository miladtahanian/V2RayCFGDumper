import yaml
import json

# Path to your YAML file
yaml_file = "AzadNet_META_IRAN-Direct.yml"

# Open the YAML file in read mode
with open(yaml_file, 'r', encoding="utf-8") as file:
  # Load the YAML data into a Python object
  data = yaml.safe_load(file)

# Open a new file for writing JSON data (optional)
with open("config.json", 'w') as json_file:
  # Dump the Python object to a JSON file with indentation (optional)
  json.dump(data, json_file, indent=2)

# Alternatively, convert to a JSON string
json_string = json.dumps(data)
# You can now use the json_string variable for further processing
