#!/usr/bin/env python3
import sys
import socket
import subprocess


# The function returns the URL availability execution code.
def check_url(url):
    return subprocess.run(['curl', '-Is', url],
                          stdout=subprocess.DEVNULL).returncode


# The function returns an array of the dictionary type in the form
# {<URL>: <IP>,....}. Argument: an array of the URL list type.
def get_url_ip(url_list):
    url_ip = {}
    len_url_list = len(url_list)
    for count in range(len_url_list):
        # Checking the existence of a URL
        if check_url(url_list[count]) == 0:
            # Checking the availability of an existing URL and
            # and form an array
            r = 0
            while r == 0:
                try:
                    url_ip[str(url_list[count])] = socket.gethostbyname(str(url_list[count]))
                    r = 1
                except Exception:
                    r = 0
    return dict(url_ip)


cnt_ask = 0
print('-' * 40)
while True:
    if cnt_ask == 0:
        # We get and output the first result without comparing the IP
        url_ip_dict = get_url_ip(sys.argv)
        for item_key in url_ip_dict.keys():
            result = item_key + " - " + url_ip_dict[item_key]
            print(result)
        url_ip_dict_coll = url_ip_dict
        cnt_ask = 1
    else:
        # We get and output the result after comparing the IP
        cnt_r = 0
        while cnt_r == 0:
            try:
                url_ip_dict = get_url_ip(sys.argv)
                cnt_r = 1
            except Exception:
                cnt_r = 0
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
