
import binancereq

class P2PAnal:

    def __init__(self):
        self.advertiser_link = None
        self.type_of_bank = None
        self.quantity = None
        self.buy_btc_price= None
        self.requester = binancereq.ALLRequest()
        self.spisok_currency = []
        self.usdt_price_maker = []
        self.usdt_price = None

    def main_analisys(self):
        self.json = self.requester.request()
        self.json2 = self.requester.request2()
        for i in self.json:
            for k in i['data']:
                self.spisok_currency.append(k['adv']['price'])
        index = self.spisok_currency.index(min(self.spisok_currency))
        self.buy_btc_price = min(self.spisok_currency)
        for i in self.json2:
            for k in i['data']:
                self.usdt_price_maker.append(k['adv']['price'])
        self.usdt_price = max(self.usdt_price_maker)

        for i in self.json[index]['data']:
            self.asset = i['adv']['asset']
            #self.advertiser_link = "https://p2p.binance.com/en/advertiserDetail" \
                                   #"?advertiserNo=" + i['advertiser']['userNo']
            self.type_of_bank = [k['identifier'] for  k in i['adv']['tradeMethods']]
            self.quantity = i['adv']['dynamicMaxSingleTransAmount']
            self.dynamicMaxSingleTransQuantity = i ['adv']['dynamicMaxSingleTransQuantity']

        return self.buy_btc_price, self.dynamicMaxSingleTransQuantity, self.asset, self.quantity, self.type_of_bank, self.usdt_price


