
import requests
import json

import Reqddata_currency
import Reqdata_usdt

class ALLRequest:
    def request(self):
        URL = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
        request = requests.post(URL, json=Reqddata_currency.data)
        request2 = requests.post(URL, json=Reqddata_currency.data2)
        request3 = requests.post(URL, json=Reqddata_currency.data3)
        self.json = json.loads(request.text)
        self.json2 =json.loads(request2.text)
        self.json3 = json.loads(request3.text)
        return self.json, self.json2, self.json3

    def request2(self):
        URL = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
        request4 = requests.post(URL, json=Reqdata_usdt.data1)
        request5 = requests.post(URL, json=Reqdata_usdt.data2)
        request6 = requests.post(URL, json=Reqdata_usdt.data3)
        self.json4 = json.loads(request4.text)
        self.json5 = json.loads(request5.text)
        self.json6 = json.loads(request6.text)
        return  self.json4, self.json5, self.json6


