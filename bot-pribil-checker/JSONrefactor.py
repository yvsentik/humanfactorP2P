import json
class Jsonchik:

    def __init__(self, message):
        self.price = None
        self.symbol = None
        self.data = json.loads(message)

    def datas(self):
        self.symbol = self.data['s']
        self.price = float(self.data['p'])
        return self.symbol, self.price
