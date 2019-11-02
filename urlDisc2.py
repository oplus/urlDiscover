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
    if r.status_code:
        good_urls.append(url)
    print(r.status_code, "---",url)


list_of_urls = combine("ip.txt", "cfg.txt")[:10]

start_time = time.time()


with ThreadPoolExecutor(max_workers=50) as pool:
    try:
        pool.map(get_url,list_of_urls)
    except KeyboardInterrupt:
        produce()
        sys.exit(1)
    finally:
        produce()

def produce():
    with open('good.txt', 'a') as good:
        for url in good_urls:
            good.write(url+'\n')


print("--- %s seconds ---" % (time.time() - start_time))
