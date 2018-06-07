#!/usr/bin/env python3

import sys, getopt
import socket

def run():
    try:
        opts, args = getopt.getopt(sys.argv[1:],None,longopts=['host=', 'port='])
    except getopt.GetoptError:
        print('Parameter Error')
    for o,a in opts:
        if o == '--host':
            host = a
        if o == '--port':
            port = a

    try:
        lst_host = host.split('.')
        lst_port = port.split('-')
        if len(lst_host) != 4 or args or len(lst_port) != 2 :
            raise ValueError
        else:
            for i in lst_host:
                if int(i) < 0:
                    raise ValueError
            port_h = int(lst_port[1])
            port_l = int(lst_port[0])
            if port_h < 0 or port_l < 0 or port_h < port_l:
                raise ValueError
    except (ValueError, TypeError):
        print('Parameter Error')
        exit()
        
    s = socket.socket()
    s.settimeout(0.1)
    for i in range(port_l,port_h+1):
        try:
            s.connect((host, i))
            print(str(i)+' open')
        except:
            print(str(i)+' closed')
            continue

if __name__ == '__main__':
    run()
