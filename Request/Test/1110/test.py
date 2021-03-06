#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/10 13:35
# @Author  : zc
# @File    : test.py

import requests
import yaml
import os


path = os.path.dirname(os.path.abspath(__file__))
yamlPath = path + "/data/zijin2-0.yaml"

with open(yamlPath,'r',encoding='utf-8') as file :
    data = yaml.load(file)


yamlData = data['addFundsPayOrder']
url = yamlData['url']
headers = yamlData['headers']
payloadStr = str(yamlData['payload'])

# B2B发送到资金管理的业务单号
list = ["ZC20201118000002"]

for i in list:
    payloadDict = eval(payloadStr.replace("FK20201110000017",i))
    r = requests.post(url,params=payloadDict,headers=headers).json()
    print(r['msg'])