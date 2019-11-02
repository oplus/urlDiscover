from urlparse import urlparse
from threading import Thread
import httplib, sys
from Queue import Queue
import time
import sys

concurrent = 200

def doWork():
    while True:
        url = q.get()
        status, url = getStatus(url)
        doSomethingWithResult(status, url)
        q.task_done()

def getStatus(ourl):
    try:
        url = urlparse(ourl)
        conn = httplib.HTTPConnection(url.netloc)
        conn.request("HEAD", url.path)
        res = conn.getresponse()
        return res.status, ourl
    except:
        return "error", ourl

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

try:
    for url in combine(sys.argv[1], sys.argv[2]):
        q.put(url.strip())
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
print("--- %s seconds ---" % (time.time() - start_time))
