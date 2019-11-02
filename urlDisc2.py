import requests
from concurrent.futures import ThreadPoolExecutor
import time


good_urls = []

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
    r = requests.head(url)
    if r.status_code == 200:
        good_urls.append(urls)
    print(r.status_code, "---",url)


list_of_urls = combine("ip.txt", "cfg.txt")

start_time = time.time()

with ThreadPoolExecutor(max_workers=100) as pool:
    pool.map(get_url,list_of_urls)

with open('good.txt', 'a') as good:
    for url in good_urls:
        good.write(url+'\n')


print("--- %s seconds ---" % (time.time() - start_time))
