import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
import pytz
import jdatetime



webpage_addresses = [
    "https://web.telegram.org/k/#?tgaddr=tg%3A%2F%2Fresolve%3Fdomain%3Dinternet_groups",
    "https://t.me/s/VPN_Xpace",
    "https://t.me/s/kingspeedchanel",
    "https://t.me/s/FreakConfig",
    "https://t.me/s/v2rayngvpn",
    "https://t.me/s/V2RAYROZ",
    "https://t.me/s/V2ray_Alpha",
    "https://t.me/s/v2_Hub",
    "https://t.me/s/Powerful1VPN"
]


def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


html_pages = []

for url in webpage_addresses:
    response = requests.get(url)
    html_pages.append(response.text)

codes = []

for page in html_pages:
    soup = BeautifulSoup(page, 'html.parser')
    code_tags = soup.find_all('code')

    for code_tag in code_tags:
        code_content = code_tag.text.strip()
        if "vless://" in code_content or "ss://" in code_content or "vmess://" in code_content or "trojan://" in code_content:
            codes.append(code_content)

codes = list(set(codes))  # Remove duplicates

processed_codes = []

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

# Combine the strings to form the final result
final_string = f"{current_day} - {current_month} | {updated_hour}:{updated_minute}"
config_string = "#✅ " + str(final_string) + "-"

for code in codes:
    vmess_parts = code.split("vmess://")
    vless_parts = code.split("vless://")

    for part in vmess_parts + vless_parts:
        if "ss://" in part or "vmess://" in part or "vless://" in part or "trojan://" in part:
            service_name = part.split("serviceName=")[-1].split("&")[0]
            processed_part = part.split("#")[0]
            processed_codes.append(processed_part)

processed_codes = remove_duplicates(processed_codes)

i = 0
with open("config.txt", "w", encoding="utf-8") as file:
    for code in processed_codes:
        if i == 0:
            config_string = "#🌐 به روزرسانی شده در" + final_string + " | هر 10 دقیقه کانفیگ جدید داریم"
        else:
            config_string = "#🌐سرور |  " + str(i) + " | " + str(final_string) + "| TAHANIANSERVERS"
        config_final = code + config_string
        file.write(config_final + "\n")
        i += 1
