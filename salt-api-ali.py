#!/usr/local/server/python27/bin/python
#-*- coding: utf-8 -*-

import requests
import json
import urllib3
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning


#首先获得salt的token
def Get_token():
    #关闭https警告信息
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    URL = 'https://101.200.128.177:443/login'
    #Hander = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    #        "Accept":"application/x-yaml"}
    Info = {'username':'saltapi','password':'1P9lS57ZaJ59FFdayuiX','eauth':'pam'}
    request = requests.post(url=URL,data=Info,verify=False)
    response = request.json()
    return response['return'][0]['token']

def salt_command():
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    tgt = sys.argv[1]
    arg = sys.argv[2]
    Url = 'https://101.200.128.177'
    Hander = {'X-Auth-Token':Get_token()}
    Data = {'client': 'local', 'tgt': tgt,'fun': 'cmd.run','arg':arg}
    ret = requests.post(url=Url,data=Data,headers=Hander,verify=False)
    print(ret.json())

if __name__ == '__main__':
    salt_command()

