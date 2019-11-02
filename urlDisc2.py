import requests
from concurrent.futures import ThreadPoolExecutor
import time




def combine(ipFile, cfgFile):
    with open("ip.txt", 'r') as ip:
        ipList = [link.strip() for link in ip.readlines()]
    with open("cfg.txt", 'r') as ip:
        cfgList = [link.strip() for link in ip.readlines()]
    combined = []
    for cfg in cfgList:
        for ip in ipList:
            combined.append(ip+cfg)
    return combined

def get_url(url):
    r = requests.get(url)
    print(r.status_code, "---",url)


list_of_urls = combine("ip.txt", "cfg.txt")[:10]

start_time = time.time()

with ThreadPoolExecutor(max_workers=100) as pool:
    pool.map(get_url,list_of_urls)

print("--- %s seconds ---" % (time.time() - start_time))
