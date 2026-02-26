import requests
import jdatetime
import pytz
import base64
import urllib.parse

new_addresses = [
    "https://raw.githubusercontent.com/iboxz/free-v2ray-collector/main/main/mix.txt"
]

def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))

codes = []

for url in new_addresses:
    try:
        response = requests.get(url, timeout=15)
        lines = response.text.splitlines()

        for line in lines:
            line = line.strip()
            if line.startswith(("vmess://", "vless://", "ss://", "trojan://")):
                codes.append(line)
    except:
        pass

codes = remove_duplicates(codes)

current_date_time = jdatetime.datetime.now(pytz.timezone('Asia/Tehran'))
current_month = current_date_time.strftime("%b")
current_day = current_date_time.strftime("%d")
updated_hour = current_date_time.strftime("%H")
updated_minute = current_date_time.strftime("%M")

update_string = f"{current_month}-{current_day} {updated_hour}:{updated_minute}"

processed_codes = []

for i, code in enumerate(codes, start=1):

    server_name = f"MTSRVRS-{i} | {update_string}"
    encoded_name = urllib.parse.quote(server_name)

    if code.startswith(("vless://", "trojan://", "ss://")):
        if "#" in code:
            code = code.split("#")[0]
        code = code + "#" + encoded_name

    processed_codes.append(code)

subscription_text = "\n".join(processed_codes)
subscription_base64 = base64.b64encode(subscription_text.encode("utf-8")).decode("utf-8")

with open("sub.txt", "w", encoding="utf-8") as file:
    file.write(subscription_base64)

print("Subscription file created successfully: sub.txt")