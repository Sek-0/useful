#!/usr/bin/python3

import sys                                                                    # sys is used there for argv
import requests                                                               # requests is used to make requests to a giver url
import urllib3                                                                # this library is to manage urls (here used to disble https errors)


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"} # pass all the requests through Burpsuite (or any proxy)

def banner():
    print('               ____                                              ')          
    print('              |  _ \ ___  ___ _ __   ___  _ __  ___  ___         ')
    print('              | |_) / _ \/ __| \'_ \ / _ \| \'_ \/ __|/ _ \      ')
    print('              |  _ <  __/\__ \ |_) | (_) | | | \__ \  __/        ')
    print('              |_| \_\___||___/ .__/ \___/|_| |_|___/\___|        ')
    print('                             |_|                                 ')
    print('                   ____ _               _                        ')
    print('                  / ___| |__   ___  ___| | _____ _ __            ')    
    print('                 | |   | \'_ \ / _ \/ __| |/ / _ \ \'__|         ')  
    print('                 | |___| | | |  __/ (__|   <  __/ |              ')
    print('                  \____|_| |_|\___|\___|_|\_\___|_|              ')
                                                          

def request(line):
    x = requests.get(line, allow_redirects=False, verify=False, proxies=proxies)
    print(x.status_code,' : ',line)

def Check_url(url): 
    try:                                           
        url = open(url, 'r')
        read_url = url.readlines()
        url_nb = 0
        for line in read_url:
            url_nb = url_nb + 1
            request(line)
    except:
        line = sys.argv[1]
        request(line)
    

if __name__== '__main__':
    

    banner()
    print('\n\n')

    try:
        url = sys.argv[1]
        Check_url(url)
    except IndexError:
        print ('/!\\ Usage : %s [URL_LIST] or [URL] \n' % sys.argv[0])
        print ('/!\\ Exemple : %s url.txt' % sys.argv[0])
        sys.exit(-1)
    except requests.exceptions.MissingSchema:
        print('/!\\ The format needed is "http(s)://exemple.com"')
        sys.exit(-1)
