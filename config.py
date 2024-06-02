import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone
import pytz
import jdatetime

webpage_addresses = [
    "https://t.me/s/piazshekan"
    "https://t.me/s/Free_Internet_Iran"
    "https://t.me/s/ARv2ray",
    "https://t.me/s/VPNCUSTOMIZE",
    "https://t.me/s/UnlimitedDev",
    "https://t.me/s/v2rayngvpn",
    "https://t.me/s/DIGIV2RAY",
    "https://t.me/s/V2RAXX",
    "https://t.me/s/ipV2Ray",
    "https://t.me/s/VPN_Xpace",
    "https://t.me/s/oneclickvpnkeys",
    "https://t.me/s/DirectVPN",
    "https://t.me/s/Parsashonam",
    "https://t.me/s/V2rayNGmat",
    "https://t.me/s/fnet00",
    "https://t.me/s/Outline_Vpn",
    "https://t.me/s/azadi_az_inja_migzare",
    "https://t.me/s/vmess_vless_v2rayng",
    "https://t.me/s/v2ray_vpn_ir",
    "https://t.me/s/BestV2rang",
    "https://t.me/s/v2logy",
    "https://t.me/s/Awlix_V2RAY",
    "https://t.me/s/reality_daily",
    "https://t.me/s/DeamNet_Proxy",
    "https://t.me/s/vpn_go67",
    "https://t.me/s/SafeNet_Server",
    "https://t.me/s/mahvarehnewssat",
    "https://t.me/s/sinabigo",
    "https://t.me/s/FAKEOFTVC",
    "https://t.me/s/customv2ray",
    "https://t.me/s/rxv2ray",
    "https://t.me/s/MTConfig",
    "https://t.me/s/MehradLearn",
    "https://t.me/s/v2Line",
    "https://t.me/s/v2rayNG_Matsuri",
    "https://t.me/s/Helix_Servers",
    "https://t.me/s/EUT_VPN",
    "https://t.me/s/proxy_mtm",
    "https://t.me/s/eliya_chiter0",
    "https://t.me/s/melov2ray",
    "https://t.me/s/servermomo",
    "https://t.me/s/vless_vmess",
    "https://t.me/s/GozargahVPN",
    "https://t.me/s/V2rayCollector",
    "https://t.me/s/v2rayng_config_amin",
    "https://t.me/s/VPNCLOP",
    "https://t.me/s/DarkTeam_VPN",
    "https://t.me/s/ProxyForOpeta",
    "https://t.me/s/Outlinev2rayNG",
    "https://t.me/s/v2_team",
    "https://t.me/s/VpnFreeSec",
    "https://t.me/s/freeconfigv2",
    "https://t.me/s/hcv2ray",
    "https://t.me/s/NIM_VPN_ir",
    "https://t.me/s/Capital_NET",
    "https://t.me/s/v2ray_swhil",
    "https://t.me/s/XsV2ray",
    "https://t.me/s/V2parsin",
    "https://t.me/s/EliV2ray",
    "https://t.me/s/proxyymeliii",
    "https://t.me/s/V2rayCollectorDonate",
    "https://t.me/s/DigiV2ray",
    "https://t.me/s/free_v2rayyy",
    "https://t.me/s/yaney_01",
    "https://t.me/s/ShadowProxy66",
    "https://t.me/s/MrV2Ray",
    "https://t.me/s/V2rayNGn",
    "https://t.me/s/V2pedia",
    "https://t.me/s/FalconPolV2rayNG",
    "https://t.me/s/CUSTOMVPNSERVER",
    "https://t.me/s/MsV2ray",
    "https://t.me/s/ServerNett",
    "https://t.me/s/lrnbymaa",
    "https://t.me/s/Proxy_PJ",
    "https://t.me/s/vmessorg",
    "https://t.me/s/polproxy",
    "https://t.me/s/v2rayng_vpnrog",
    "https://t.me/s/lightning6",
    "https://t.me/s/frev2ray",
    "https://t.me/s/proxy_kafee",
    "https://t.me/s/Qv2rayDONATED",
    "https://t.me/s/Capoit",
    "https://t.me/s/PrivateVPNs",
    "https://t.me/s/Cov2ray",
    "https://t.me/s/kiava",
    "https://t.me/s/prrofile_purple",
    "https://t.me/s/nofiltering2",
    "https://t.me/s/FreeV2rays",
    "https://t.me/s/configV2rayNG",
    "https://t.me/s/vpnmasi",
    "https://t.me/s/v2ray_ar",
    "https://t.me/s/iSeqaro",
    "https://t.me/s/God_CONFIG",
    "https://t.me/s/vpn_ioss",
    "https://t.me/s/AliAlma_GSM",
    "https://t.me/s/v2rayng_org",
    "https://t.me/s/flyv2ray",
    "https://t.me/s/v2ray_outlineir",
    "https://t.me/s/v2_vmess",
    "https://t.me/s/FreeVlessVpn",
    "https://t.me/s/freeland8",
    "https://t.me/s/vmessiran",
    "https://t.me/s/vmessq",
    "https://t.me/s/WeePeeN",
    "https://t.me/s/V2rayNG3",
    "https://t.me/s/ShadowsocksM",
    "https://t.me/s/shadowsocksshop",
    "https://t.me/s/v2rayan",
    "https://t.me/s/ShadowSocks_s",
    "https://t.me/s/VmessProtocol",
    "https://t.me/s/napsternetv_config",
    "https://t.me/s/Easy_Free_VPN",
    "https://t.me/s/V2Ray_FreedomIran",
    "https://t.me/s/V2RAY_VMESS_free",
    "https://t.me/s/v2ray_for_free",
    "https://t.me/s/V2rayN_Free",
    "https://t.me/s/free4allVPN",
    "https://t.me/s/vpn_ocean",
    "https://t.me/s/configV2rayForFree",
    "https://t.me/s/v2rayNG_VPN",
    "https://t.me/s/freev2rayssr",
    "https://t.me/s/v2rayn_server",
    "https://t.me/s/Shadowlinkserverr",
    "https://t.me/s/iranvpnet",
    "https://t.me/s/vmess_iran",
    "https://t.me/s/mahsaamoon1",
    "https://t.me/s/V2RAY_NEW",
    "https://t.me/s/v2RayChannel",
    "https://t.me/s/config_v2ray",
    "https://t.me/s/vpn_proxy_custom",
    "https://t.me/s/v2ray_custom",
    "https://t.me/s/HTTPCustomLand",
    "https://t.me/s/ViPVpn_v2ray",
    "https://t.me/s/FreeNet1500",
    "https://t.me/s/beta_v2ray",
    "https://t.me/s/vip_vpn_2022",
    "https://t.me/s/FOX_VPN66",
    "https://t.me/s/VorTexIRN",
    "https://t.me/s/YtTe3la",
    "https://t.me/s/V2RayOxygen",
    "https://t.me/s/Network_442",
    "https://t.me/s/VPN_443",
    "https://t.me/s/v2rayng_v",
    "https://t.me/s/ultrasurf_12",
    "https://t.me/s/frev2rayng",
    "https://t.me/s/FreakConfig",
    "https://t.me/s/Awlix_ir",
    "https://t.me/s/Configforvpn01",
    "https://t.me/s/v2rayvpnchannel",
    "https://t.me/s/v2rayfree1",
    "https://t.me/s/nx_v2ray",
    "https://t.me/s/nufilter",
    "https://t.me/s/Free_HTTPCustom",
    "https://t.me/s/vpn_Nv1",
    "https://t.me/s/shopingv2ray",
    "https://t.me/s/MT_TEAM_IRAN",
    "https://t.me/s/V2ray_Team",
    "https://t.me/s/VpnProsecc",
    "https://t.me/s/ConfigsHUB",
    "https://t.me/s/VlessConfig",
    "https://t.me/s/kingofilter",
    "https://t.me/s/IRN_VPN",
    "https://t.me/s/V2raysFree",
    "https://t.me/s/SvnTeam",
    "https://t.me/s/free1_vpn",
    "https://t.me/s/vpn_xw",
    "https://t.me/s/V2RayTz",
    "https://t.me/s/OutlineVpnOfficial",
    "https://t.me/s/mehrosaboran",
    "https://t.me/s/mftizi",
    "https://t.me/s/https_config_injector",
    "https://t.me/s/Hope_Net",
    "https://t.me/s/V2rayng_Fast",
    "https://t.me/s/DailyV2RY",
    "https://t.me/s/shh_proxy",
    "https://t.me/s/forwardv2ray",
    "https://t.me/s/Lockey_vpn",
    "https://t.me/s/shadow_socks1",
    "https://t.me/s/Everyday_VPN",
    "https://t.me/s/v2ray1_ng",
    "https://t.me/s/Romax_VPN",
    "https://t.me/s/DeamNet_proxy",
    "https://t.me/s/socks5tobefree",
    "https://t.me/s/V_2rey",
    "https://t.me/s/teamkingo",
    "https://t.me/s/spdnet",
    "https://t.me/s/TunelProV2",
    "https://t.me/s/iran_v2ray1",
    "https://t.me/s/v2rayvpn2",
    "https://t.me/s/v2rayNgg_iran",
    "https://t.me/s/V2rayNG_account_free",
    "https://t.me/s/V2rayi_net",
    "https://t.me/s/vpnowl",
    "https://t.me/s/ghalagyann",
    "https://t.me/s/XpnTeam",
    "https://t.me/s/fhkllvjkll",
    "https://t.me/s/V2ray_Alpha",
    "https://t.me/s/IRANVPNNET",
    "https://t.me/s/GH_v2rayng",
    "https://t.me/s/VPNwedbaz",
    "https://t.me/s/icv2ray",
    "https://t.me/s/iTV2RAY",
    "https://t.me/s/ArV2ray",
    "https://t.me/s/SEVEN_ping",
    "https://t.me/s/meli_proxyy",
    "https://t.me/s/SafeNetIR",
    "https://t.me/s/V2RAYROZ",
    "https://t.me/s/V2Graphy",
    "https://t.me/s/svn3team",
    "https://t.me/s/v20reyng",
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
            config_string = "#🌐 به روزرسانی شده در" + final_string + " | هر 6 ساعت کانفیگ جدید داریم"
        else:
            config_string = "#🌐سرور " + str(i) + " | " + str(final_others_string) + "| MTSRVRS"
        config_final = code + config_string
        file.write(config_final + "\n")
        i += 1
