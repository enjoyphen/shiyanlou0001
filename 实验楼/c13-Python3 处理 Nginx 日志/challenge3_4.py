#!/usr/bin/env python3


import re
from datetime import datetime

# use re expressin to parse log file, return data list
def open_parser(filename):
    with open(filename) as logfile:
# re pattern
        pattern = (r''
                   r'(\d+.\d+.\d+.\d+)\s-\s-\s' # IP address
                   r'\[(.+)\]\s' # time
                   r'"GET\s(.+)\s\w+/.+"\s' # request path
                   r'(\d+)\s' # status cod
                   #r'(\d+)\s' # datasize
                   #r'"(.+)"\s' # header
                   #r'"(.+)"' # client information
                   )
        parsers = re.findall(pattern,logfile.read())
        return parsers

def main():
    #
    logs = open_parser('/home/shiyanlou/Code/nginx.log')
    url_dict={}
    ip_dict = {}
    j = 0
    for i in logs:
        ip, url, s_code = i[0], i[2], i[3]
        try:
            ip_dict[ip] += 1
        except KeyError:
            ip_dict[ip] = 1 
        if i[3] == '404':
            if url == '/favicon.ico':
                j+=1
            try:
                url_dict[url] += 1
            except KeyError:
                url_dict[url] = 1
    lst_ip = sorted(ip_dict.items(), key=lambda x:x[1], reverse=True)
    lst_url = sorted(url_dict.items(), key=lambda x:x[1], reverse=True)
    #url_dict = ip_dict ={}-->the dict value will be the same finllay
    url_dict = {}
    ip_dict = {}
    url_dict[lst_url[0][0]] = lst_url[0][1]
    ip_dict[lst_ip[0][0]] = lst_ip[0][1]

    return ip_dict, url_dict

if __name__ =='__main__':
    ip_dict, url_dict = main()
    print(ip_dict, url_dict)
