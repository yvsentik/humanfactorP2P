import websocket

import JSONrefactor
import P2PAnalytics
import Terpenie

class ATAS:
    def __init__(self):
        self.buy = None
        self.sell = None
        self.b = None

    def websoset(self):
        socket = 'wss://stream.binance.com:9443/ws/btcusdt@aggTrade'
        ws = websocket.WebSocketApp(socket, on_message=self.on_message, on_close=self.on_close)
        ws.run_forever()

    def on_message(self, ws, message):
        data = JSONrefactor.Jsonchik(message)
        data.datas()
        b = data.price
        a = P2PAnalytics.P2PAnal()
        result = a.main_analisys()
        quantity = float(result[1])
        spred = (((b*quantity*float(result[5])-float(result[3]))/float(result[3]))*100)
        if (b*quantity*float(result[5])-float(result[3]))>100:
            k = f"По цене {result[0]}, купи {result[1]} {result[2]},  потрать {float(result[3])}, через {result[4]}, \n продай {result[1]} по {b} usdt, продай usdt по {float(result[5])} \n получи {b*quantity*float(result[5])} \n spred:{round(spred,2)}% \n слить в ноль по курсу: {float(result[0])/float(result[5])}"
            print(k)
            Terpenie.send_data(k)




        #print("Актуальная цена битка", b)
        #print(f"Поставь лимит по {b} и продай как мейкер по {result[1]}")
        # currently price from websocket
        #sell = binancereq.ALLRequest()
        #self.sell = sell.request()
        #print(self.sell)
        #a = Analytics.Analytics( )
        #a.setatt(self.sell[0], self.sell[1], self.b, self.sell[2], self.sell[3])
        #a.ret()
    def on_close(ws):
        print('VSE')


