import requests
import ruamel
from datetime import datetime, timezone
import jdatetime
from ruamel.yaml import YAML
import pytz

# Retrieve the YAML file from the URL
url = 'https://raw.githubusercontent.com/AzadNetCH/Clash/main/AzadNet_META_IRAN-Direct.yml'  # Replace with the actual URL
response = requests.get(url)
yaml = YAML(typ='rt')  # Using round-trip mode for loading
data = yaml.load(response.text)

# Get the current date and time
current_date_time = jdatetime.datetime.now(pytz.timezone('Asia/Tehran'))
# Print the current month in letters
current_month = current_date_time.strftime("%b")

# Get the current day as a string
current_day = current_date_time.strftime("%d")

# Increase the current hour by 4 hours
#new_date_time = current_date_time + timedelta(hours=4)

# Get the updated hour as a string
updated_hour = current_date_time.strftime("%H")

updated_minute = current_date_time.strftime("%M")

final_string = f"{current_month}-{current_day} | {updated_hour}:{updated_minute}"

config_string = "#🌐 به روزرسانی شده در" + final_string + "TAHANIANSRVRS"
# Replace the text
# data = str(data).replace('(AzadNet.t.me)',"")
# Save the modified data back to a file
with open('config.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(data, file)