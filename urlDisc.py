#from urlparse import urlparse
import urllib.parse
from threading import Thread
import http.client, sys
from queue import Queue
import time
import requests

concurrent = 200

def doWork():
    while True:
        url = q.get()
        status = getStatus(url)
        #doSomethingWithResult(status, url)
        q.task_done()

def getStatus(ourl):

    try:
        r = requests.get(ourl)
        print(r.status_code, ourl)
    except:
        print("Error", ourl)


def doSomethingWithResult(status, url):
    print(status, url)

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()

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

#print(combine('ip.txt', 'cfgFile.txt'))  ###for testing
start_time = time.time()
try:
    for url in combine("ip.txt", "cfg.txt")[:100]: #####################Change this line
        q.put(url.strip())
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
print("--- %s seconds ---" % (time.time() - start_time))
