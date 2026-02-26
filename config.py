import requests
import jdatetime
import pytz

new_addresses = [
    "https://raw.githubusercontent.com/iboxz/free-v2ray-collector/main/main/mix.txt"
]

def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))

codes = []

for url in new_addresses:
    response = requests.get(url)
    lines = response.text.splitlines()

    for line in lines:
        line = line.strip()
        if line.startswith(("vmess://", "vless://", "ss://", "trojan://")):
            codes.append(line)

codes = remove_duplicates(codes)

# تاریخ
current_date_time = jdatetime.datetime.now(pytz.timezone('Asia/Tehran'))
current_month = current_date_time.strftime("%b")
current_day = current_date_time.strftime("%d")
updated_hour = current_date_time.strftime("%H")
updated_minute = current_date_time.strftime("%M")

final_string = f"{current_month}-{current_day} | {updated_hour}:{updated_minute}"
final_others_string = f"{current_month}-{current_day}"

with open("config.txt", "w", encoding="utf-8") as file:
    for i, code in enumerate(codes):
        if i == 0:
            config_string = "#🌐 به روزرسانی شده در " + final_string + " | هر 15 دقیقه کانفیگ جدید داریم"
        else:
            config_string = "#🌐 سرور " + str(i) + " | " + final_others_string + " | MTSRVRS"
        
        file.write(code + config_string + "\n")