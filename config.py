import yaml
import requests
import jdatetime
import pytz

def replace_in_yaml(source_file, target_file, replacements, encoding="utf-8"):
  try:
    if source_file.startswith("http"):
      yaml_data = download_yaml_from_url(source_file, encoding)
    else:
      with open(source_file, 'r', encoding=encoding) as file:
        yaml_data = file.read()
    data = yaml.safe_load(yaml_data)
    def replace_strings(data, replacements):
      if isinstance(data, str):
        for key, value in replacements.items():
          data = data.replace(key, value)
      elif isinstance(data, (list, dict)):
        if isinstance(data, list):
          new_list = []
          for item in data:
            new_list.append(replace_strings(item, replacements.copy()))
          data = new_list
        else:
          for key, value in data.items():
            data[key] = replace_strings(value, replacements.copy())
      return data
    data = replace_strings(data, replacements.copy())  
    with open(target_file, 'w', encoding=encoding) as file:
      yaml.dump(data, file, indent=2)
    print(f"Successfully replaced strings in YAML from {source_file}")
    print(f"Saved to: {target_file}")
  except (IOError, UnicodeDecodeError, requests.exceptions.RequestException) as e:
    print(f"Error processing YAML: {e}")
def download_yaml_from_url(url, encoding):
  response = requests.get(url)
  response.raise_for_status()
  return response.content.decode(encoding)
current_date_time = jdatetime.datetime.now(pytz.timezone('Asia/Tehran'))
current_month = current_date_time.strftime("%b")
current_day = current_date_time.strftime("%d")
updated_hour = current_date_time.strftime("%H")
updated_minute = current_date_time.strftime("%M")
final_string = f"{current_month}-{current_day} | {updated_hour}:{updated_minute}"
final_others_string = f"{current_day}-{current_month}"
config_string = str(final_string) + "- TAHANIANSRVRS"
source_file = "https://raw.githubusercontent.com/AzadNetCH/Clash/main/AzadNet_META_IRAN-Direct.yml"
target_file = "config.yml"
replacements = {"AzadNet.t.me": config_string}
encoding = "utf-8"

replace_in_yaml(source_file, target_file, replacements, encoding)
