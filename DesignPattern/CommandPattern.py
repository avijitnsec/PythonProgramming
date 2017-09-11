class Order:
    def execute(self):
        raise NotImplementedError('Need to Implement !')


class Stock:
    stock_name = ''
    quantity = ''

    def __init__(self, name, quantity):
        self.stock_name = name
        self.quantity = quantity

    def buy(self):
        print("Buying stock: " + self.stock_name + "Quantity: " + self.quantity)

    def sell(self):
        print("Selling stock: " + self.stock_name + "Quantity: " + self.quantity)


class Buy(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class Sell(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


class Broker:
    list = []

    def take_order(self, obj):
        self.list.append(obj)

    def place_order(self):
        for obj in self.list:
            obj.execute()

if __name__ == '__main__':
    stk = Stock('AAPL', '10')
    b = Broker()
    b.take_order(Buy(stk))
    b.take_order(Sell(stk))
    b.place_order()