import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
import pytz
import jdatetime

addresses = [
"https://telegram.me/s/filembad",
"https://telegram.me/s/canfingV2rayNG",
"https://telegram.me/s/Alpha_V2ray_Iran",
"https://telegram.me/s/Farah_VPN",
"https://telegram.me/s/vaddress",
"https://telegram.me/s/v2ray_claim",
"https://telegram.me/s/FreakConfig",
"https://telegram.me/s/BigSmoke_Config"
]

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

html_pages = []

for url in addresses:
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

current_date_time = jdatetime.datetime.now(pytz.timezone('Asia/Tehran'))
current_month = current_date_time.strftime("%b")
current_day = current_date_time.strftime("%d")
updated_hour = current_date_time.strftime("%H")
updated_minute = current_date_time.strftime("%M")
final_string = f"{current_month}-{current_day} | {updated_hour}:{updated_minute}"
final_others_string = f"{current_month}-{current_day}"
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

new_processed_codes = []

for code in processed_codes:
    vmess_parts = code.split("vmess://")
    vless_parts = code.split("vless://")

    for part in vmess_parts + vless_parts:
        if "ss://" in part or "vmess://" in part or "vless://" in part or "trojan://" in part:
            service_name = part.split("serviceName=")[-1].split("&")[0]
            processed_part = part.split("#")[0]
            new_processed_codes.append(processed_part)

i = 0
with open("sub.txt", "w", encoding="utf-8") as file:
    for code in new_processed_codes:
        if i == 0:
            config_string = "#🌐 به روزرسانی شده در" + final_string
        else:
            config_string = "#🌐سرور " + str(i) + " | " + str(final_others_string) + "| MTSRVRS"
        config_final = code + config_string
        file.write(config_final + "\n")
        i += 1
