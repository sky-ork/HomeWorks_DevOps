#!/usr/bin/env python3
import sys
import socket
import subprocess
import time


# Adding the URL and IP from the arguments to the dict
def get_url_ip(url):
    url_ip = {}
    for count in range(len(url)):
        exit_code = subprocess.run(['curl', '-Is', str(url[count])],
                                   stdout=subprocess.DEVNULL)
        if exit_code.returncode == 0:
            url_ip[str(url[count])] = socket.gethostbyname(str(url[count]))
    return dict(url_ip)


cnt_ask = 0
print('-' * 40)
while cnt_ask < 100:
    if cnt_ask == 0:
        # We get and output the first result without comparing the IP
        url_ip_dict = get_url_ip(sys.argv)
        for item_key in url_ip_dict.keys():
            result = item_key + " - " + url_ip_dict[item_key]
            print(result)
        url_ip_dict_coll = url_ip_dict
    else:
        # We get and output the result after comparing the IP
        url_ip_dict = get_url_ip(sys.argv)
        for item_key in url_ip_dict.keys():
            if url_ip_dict[item_key] == url_ip_dict_coll[item_key]:
                result = item_key + " - " + url_ip_dict[item_key]
                print(result)
            else:
                result = "[ERROR] " + item_key + " IP mismatch: " \
                         + url_ip_dict_coll[item_key] + " --> " \
                         + url_ip_dict[item_key]
                print(result)
        url_ip_dict_coll = url_ip_dict
    print('-' * 40)
    cnt_ask += 1
    time.sleep(1)
