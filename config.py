import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
import pytz
import jdatetime

old_webpage_addresses = [
        "https://t.me/s/v2ray_configs_pool",
    "https://t.me/s/XpnTeam",
    "https://t.me/v2rayNGcloud",
    "https://t.me/s/ZibaNabz",
    "https://t.me/s/FreakConfig",
    "https://t.me/s/V_2rey",
    "https://t.me/s/V2ray_Alpha",
    "https://t.me/s/PROXY_MTM",
    "https://t.me/s/SiNABiGO",
    "https://t.me/s/v2rayng12023",
    "https://t.me/s/vlessconfig",
    "https://t.me/s/piazshekan",
    "https://t.me/s/Free_Internet_Iran",
    "https://t.me/s/ARv2ray",
    "https://t.me/s/VPNCUSTOMIZE",
    "https://t.me/s/UnlimitedDev",
    "https://t.me/s/MARAMBASHI",
    "https://t.me/s/PrivateVPNs",
    "https://t.me/s/client_proo",
    "https://t.me/s/nufilter",
    "https://t.me/s/icv2ray",
    "https://t.me/s/Vpn_Mikey",
    "https://t.me/s/v2rayngvpn",
    "https://t.me/s/kingspeedchanel",
    "https://t.me/s/VPN_Xpace",
    "https://t.me/s/SVNTEAM",
    "https://t.me/s/WPSNET",
    "https://t.me/s/v2rayng_fa2",
]

webpage_addresses = [
    "https://t.me/s/Hope_Net",
    "https://t.me/s/ServerNett",
    "https://t.me/s/alfred_config",
    "https://t.me/s/allv2ray",
    "https://t.me/s/alo_v2rayng",
    "https://t.me/s/angus_vpn",
    "https://t.me/s/antifilterservice",
    "https://t.me/s/arv2ray",
    "https://t.me/s/asak_vpn",
    "https://t.me/s/asintech",
    "https://t.me/s/astrovpn_official",
    "https://t.me/s/awlix_ir",
    "https://t.me/s/azarbayjab1",
    "https://t.me/s/bermudavpn24",
    "https://t.me/s/bigsmoke_config",
    "https://t.me/s/blueberrynetwork",
    "https://t.me/s/bored_vpn",
    "https://t.me/s/catvpns",
    "https://t.me/s/cconfig_v2ray",
    "https://t.me/s/city_v2rayng",
    "https://t.me/s/configforvpn",
    "https://t.me/s/configpositive",
    "https://t.me/s/configt",
    "https://t.me/s/configv2rayforfree",
    "https://t.me/s/custom_config",
    "https://t.me/s/customizev2ray",
    "https://t.me/s/cvrnet",
    "https://t.me/s/dailyv2ry",
    "https://t.me/s/daredevill_404",
    "https://t.me/s/deragv2ray",
    "https://t.me/s/digiv2ray",
    "https://t.me/s/directvpn",
    "https://t.me/s/donald_vpn",
    "https://t.me/s/drvpn_net",
    "https://t.me/s/easy_free_vpn",
    "https://t.me/s/entrynet",
    "https://t.me/s/ev2rayy",
    "https://t.me/s/expressvpn_420",
    "https://t.me/s/external_net",
    "https://t.me/s/farahvpn",
    "https://t.me/s/fasst_vpn",
    "https://t.me/s/fast_2ray",
    "https://t.me/s/fastkanfig",
    "https://t.me/s/fastshadow_vpn",
    "https://t.me/s/filterk0sh",
    "https://t.me/s/flyv2ray",
    "https://t.me/s/freakconfig",
    "https://t.me/s/freakconfig1",
    "https://t.me/s/freakconfig2",
    "https://t.me/s/free1_vpn",
    "https://t.me/s/free_vpn02",
    "https://t.me/s/freeconfig01",
    "https://t.me/s/freeconfigvpns",
    "https://t.me/s/freeiranweb",
    "https://t.me/s/freenapsternetv",
    "https://t.me/s/freev2raym",
    "https://t.me/s/freevirgoolnet",
    "https://t.me/s/fsv2ray",
    "https://t.me/s/ghalagyann",
    "https://t.me/s/godv2ray_ng",
    "https://t.me/s/golestan_vpn",
    "https://t.me/s/grizzlyvpn",
    "https://t.me/s/hajimamadvpn",
    "https://t.me/s/hamster_vpnn",
    "https://t.me/s/hatunnel_vpn",
    "https://t.me/s/hope_net",
    "https://t.me/s/hopev2ray",
    "https://t.me/s/hormozvpn",
    "https://t.me/s/hose_io",
    "https://t.me/s/icv2ray",
    "https://t.me/s/imrv2ray",
    "https://t.me/s/ios_v2",
    "https://t.me/s/ipcloudflaretamiz",
    "https://t.me/s/ipv2ray",
    "https://t.me/s/iranbaxvpn",
    "https://t.me/s/iraniv2ray_config",
    "https://t.me/s/irv2rey",
    "https://t.me/s/isvvpn",
    "https://t.me/s/kafing_2",
    "https://t.me/s/kingofilter",
    "https://t.me/s/lightning6",
    "https://t.me/s/ln2ray",
    "https://t.me/s/lombo_channel",
    "https://t.me/s/mahdiserver",
    "https://t.me/s/manzariyeh_rasht",
    "https://t.me/s/maznet",
    "https://t.me/s/meli_proxyy",
    "https://t.me/s/mester_v2ray",
    "https://t.me/s/mgvpnsale",
    "https://t.me/s/mikasavpn",
    "https://t.me/s/miov2ray",
    "https://t.me/s/moftinet",
    "https://t.me/s/msv2ray",
    "https://t.me/s/msv2raynp",
    "https://t.me/s/n2vpn",
    "https://t.me/s/netmellianti",
    "https://t.me/s/new_proxy_channel",
    "https://t.me/s/noforcedheaven",
    "https://t.me/s/npvv2rayfilter",
    "https://t.me/s/nufilter",
    "https://t.me/s/ohvpn",
    "https://t.me/s/orange_vpns",
    "https://t.me/s/outline_ir",
    "https://t.me/s/outline_vpn",
    "https://t.me/s/pars_vpn3",
    "https://t.me/s/parsashonam",
    "https://t.me/s/pashmam_vpn",
    "https://t.me/s/pishiserver",
    "https://t.me/s/pqv2ray",
    "https://t.me/s/privatevpns",
    "https://t.me/s/proprojec",
    "https://t.me/s/proxiiraniii",
    "https://t.me/s/proxy_n1",
    "https://t.me/s/proxyfull",
    "https://t.me/s/proxystore11",
    "https://t.me/s/prroxyng",
    "https://t.me/s/puni_shop_v2rayng",
    "https://t.me/s/qeshmserver",
    "https://t.me/s/realvpnmaster",
    "https://t.me/s/rnrifci",
    "https://t.me/s/satoshivpn",
    "https://t.me/s/savagev2ray",
    "https://t.me/s/selinc",
    "https://t.me/s/servernett",
    "https://t.me/s/shadowproxy66",
    "https://t.me/s/shokhmiplus",
    "https://t.me/s/sinavm",
    "https://t.me/s/sobi_vpn",
    "https://t.me/s/special_net8",
    "https://t.me/s/spikevpn",
    "https://t.me/s/srcvpn",
    "https://t.me/s/summertimeus",
    "https://t.me/s/superv2rang",
    "https://t.me/s/svnteam",
    "https://t.me/s/tehranargo",
    "https://t.me/s/tehranargo1",
    "https://t.me/s/thexconfig",
    "https://t.me/s/thunderv2ray",
    "https://t.me/s/tv_v2ray",
    "https://t.me/s/ultrasurf_12",
    "https://t.me/s/v2_city",
    "https://t.me/s/v2aryng_vpn",
    "https://t.me/s/v2boxvpnn",
    "https://t.me/s/v2graphy",
    "https://t.me/s/v2net_iran",
    "https://t.me/s/v2ngfast",
    "https://t.me/s/v2pedia",
    "https://t.me/s/v2ra2",
    "https://t.me/s/v2raand",
    "https://t.me/s/v2rang00",
    "https://t.me/s/v2range",
    "https://t.me/s/v2raxx",
    "https://t.me/s/v2ray1_ng",
    "https://t.me/s/v2ray6388",
    "https://t.me/s/v2ray_alpha07",
    "https://t.me/s/v2ray_configs_pool",
    "https://t.me/s/v2ray_fark",
    "https://t.me/s/v2ray_ng",
    "https://t.me/s/v2ray_one1",
    "https://t.me/s/v2ray_raha",
    "https://t.me/s/v2ray_rolly",
    "https://t.me/s/v2rayargon",
    "https://t.me/s/v2raych",
    "https://t.me/s/v2rayfast",
    "https://t.me/s/v2rayfast_7",
    "https://t.me/s/v2rayfree_irr",
    "https://t.me/s/v2rayiman",
    "https://t.me/s/v2raylandd",
    "https://t.me/s/v2rayn2g",
    "https://t.me/s/v2rayng3",
    "https://t.me/s/v2rayng_city",
    "https://t.me/s/v2rayng_madam",
    "https://t.me/s/v2rayng_prime",
    "https://t.me/s/v2rayngv",
    "https://t.me/s/v2rayngvpnn",
    "https://t.me/s/v2rayngzendegimamad",
    "https://t.me/s/v2rayprotocol",
    "https://t.me/s/v2rayyngvpn",
    "https://t.me/s/v2rez",
    "https://t.me/s/v2rray_ng",
    "https://t.me/s/v2ry_proxy",
    "https://t.me/s/v2ryng01",
    "https://t.me/s/v2ryng_vpn",
    "https://t.me/s/v2ryngfree",
    "https://t.me/s/v2safe",
    "https://t.me/s/v2safee",
    "https://t.me/s/v_2rayngvpn",
    "https://t.me/s/vip_vpn_2022",
    "https://t.me/s/vipv2rayngnp",
    "https://t.me/s/vipv2rey",
    "https://t.me/s/vipvpn_v2ray",
    "https://t.me/s/vistav2ray",
    "https://t.me/s/vlessconfig",
    "https://t.me/s/vmesc",
    "https://t.me/s/vmess_ir",
    "https://t.me/s/vmess_iran",
    "https://t.me/s/vmesskhodam",
    "https://t.me/s/vmesskhodam_vip",
    "https://t.me/s/vmessprotocol",
    "https://t.me/s/vp22ray",
    "https://t.me/s/vpfreen",
    "https://t.me/s/vpn_accounti",
    "https://t.me/s/vpn_free_v2ray5",
    "https://t.me/s/vpn_ioss",
    "https://t.me/s/vpn_kanfik",
    "https://t.me/s/vpn_mikey",
    "https://t.me/s/vpn_proxy_custom",
    "https://t.me/s/vpn_tehran",
    "https://t.me/s/vpn_vip_nor",
    "https://t.me/s/vpnazadland",
    "https://t.me/s/vpnconfignet",
    "https://t.me/s/vpnfail_v2ray",
    "https://t.me/s/vpnhubmarket",
    "https://t.me/s/vpnkanfik",
    "https://t.me/s/vpnmasi",
    "https://t.me/s/vpnowl",
    "https://t.me/s/vpnstorefast",
    "https://t.me/s/vpnv2rayngv",
    "https://t.me/s/vpnxyam_ir",
    "https://t.me/s/wedbaztel",
    "https://t.me/s/wsbvpn",
    "https://t.me/s/xpnteam",
    "https://t.me/s/xvproxy",
    "https://t.me/s/zede_filteri",
    "https://t.me/s/zibanabz",
    "https://t.me/s/zohalserver"
]

new_webaddresses = [
    "https://t.me/s/BinexTiFy",
    "https://t.me/s/VPN_ROOM",
    "https://t.me/s/VPNTV20",
    "https://t.me/s/MTMVPN",
    "https://t.me/s/MARAMBASHI",
	"https://t.me/s/zedmodeonVPN",
    "https://t.me/s/LIGHTNING6",
	"https://t.me/s/EXPRESSVPN_420",
    
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
with open("config.txt", "w", encoding="utf-8") as file:
    for code in new_processed_codes:
        if i == 0:
            config_string = "#🌐 به روزرسانی شده در" + final_string + " | هر 15 دقیقه کانفیگ جدید داریم"
        else:
            config_string = "#🌐سرور " + str(i) + " | " + str(final_others_string) + "| MTSRVRS"
        config_final = code + config_string
        file.write(config_final + "\n")
        i += 1
