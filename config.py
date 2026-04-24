import requests
from bs4 import BeautifulSoup
from datetime import timedelta
import pytz
import jdatetime
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def is_valid_code(code):
    return any(code.startswith(prefix) for prefix in ["vmess://", "vless://", "ss://", "trojan://"])

def test_http_connection(code):
    try:
        if code.startswith("ss://"):
            return True 
        elif code.startswith("vmess://") or code.startswith("vless://") or code.startswith("trojan://"):
            import base64
            try:
                data = base64.b64decode(code.split("://")[1]).decode('utf-8')
                import json
                info = json.loads(data)
                server = info.get("add")
                if not server:
                    return False
                url = f"http://google.com/"
                resp = requests.get(url, timeout=5)
                return resp.status_code == 200
            except Exception as e:
                logging.warning(f"Failed to parse or connect for code: {e}")
                return False
        else:
            return False
    except Exception as e:
        logging.warning(f"Connection test failed: {e}")
        return False

def read_addresses_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            addresses = [line.strip() for line in lines if line.strip()]
            return addresses
    except Exception as e:
        logging.error(f"Failed to read addresses file: {e}")
        return []

addresses = read_addresses_from_file("addresses.txt")

addresses = list(dict.fromkeys([a.lower() for a in addresses]))

html_pages = []

for url in addresses:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html_pages.append(response.text)
        logging.info(f"Fetched {url} successfully.")
    except requests.RequestException as e:
        logging.warning(f"Failed to fetch {url}: {e}")
        continue

codes = []

for page in html_pages:
    soup = BeautifulSoup(page, 'html.parser')
    code_tags = soup.find_all('code')

    for code_tag in code_tags:
        code_content = code_tag.text.strip()
        if any(prefix in code_content for prefix in ["vless://", "ss://", "vmess://", "trojan://"]):
            codes.append(code_content)

codes = remove_duplicates(codes)

current_date_time = jdatetime.datetime.now(pytz.timezone('Asia/Tehran'))
current_month = current_date_time.strftime("%b")
current_day = current_date_time.strftime("%d")
updated_hour = current_date_time.strftime("%H")
updated_minute = current_date_time.strftime("%M")
final_string = f"{current_month}-{current_day} | {updated_hour}:{updated_minute}"
final_others_string = f"{current_month}-{current_day}"

processed_codes = []

for code in codes:
    parts = []
    for prefix in ["vmess://", "vless://", "ss://", "trojan://"]:
        if prefix in code:
            parts += code.split(prefix)
    parts = parts[1:] if parts else []
    for part in parts:
        full_code = ""
        for prefix in ["vmess://", "vless://", "ss://", "trojan://"]:
            if code.startswith(prefix):
                full_code = prefix + part
                break
            elif prefix + part in code:
                full_code = prefix + part
                break
        if not full_code:
            full_code = part
        full_code = full_code.split("#")[0].strip()
        if is_valid_code(full_code):
            processed_codes.append(full_code)

processed_codes = remove_duplicates(processed_codes)

valid_codes = []
for code in processed_codes:
    if test_http_connection(code):
        valid_codes.append(code)
    else:
        logging.info(f"Invalid or unreachable config skipped: {code[:30]}...")

with open("sub.txt", "w", encoding="utf-8") as file:
    for i, code in enumerate(valid_codes):
        if i == 0:
            header = f"#🌐 به روزرسانی شده در {final_string} | هر 15 دقیقه کانفیگ جدید داریم"
        else:
            header = f"#🌐سرور {i} | {final_others_string} | MTSRVRS"
        file.write(code + " " + header + "\n")

logging.info(f"Total valid configs saved: {len(valid_codes)}")